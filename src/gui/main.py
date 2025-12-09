import sys
import pandas as pd
from datetime import date
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QFileDialog, QLabel, QListWidget, QListWidgetItem, QMessageBox,
    QDialog, QFormLayout, QLineEdit, QDateEdit, QDoubleSpinBox
)
from src.reformatter_core import reformat_excel, validate_columns
from src.models.goat import Goat
from src.models.exhibitor import Exhibitor
from src.models.class_entry import ClassEntry
from src.utils.date_utils import parse_dob, format_dob
from src.reports.report_generator import generate_payout_report

# ---------- Awards Loader ----------
def load_awards(file_path="data/awards.xlsx"):
    """Load placement and ribbon payouts from data/awards.xlsx."""
    try:
        df = pd.read_excel(file_path)
        placement_values = (
            df[df["Award Type"] == "Placement"]
            .set_index("Award Name")["Value"].to_dict()
        )
        ribbon_values = (
            df[df["Award Type"] == "Ribbon"]
            .set_index("Award Name")["Value"].to_dict()
        )
        return placement_values, ribbon_values
    except Exception:
        # Fallback to zeroed dictionaries if file is missing or malformed
        return {}, {}

PLACEMENT_VALUES, RIBBON_VALUES = load_awards()

# ---------- Dialogs ----------
class ExhibitorDialog(QDialog):
    """Add/Edit Exhibitor dialog with validation for last name and entry number."""

    def __init__(self, parent=None, exhibitor=None):
        super().__init__(parent)
        self.setWindowTitle("Add/Edit Exhibitor")
        layout = QFormLayout()

        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.dob = QDateEdit()
        self.dob.setCalendarPopup(True)
        self.dob.setDate(date.today())
        self.entry_number = QLineEdit()

        if exhibitor:
            self.first_name.setText(exhibitor.first_name)
            self.last_name.setText(exhibitor.last_name)
            if exhibitor.dob:
                self.dob.setDate(exhibitor.dob)
            self.entry_number.setText(exhibitor.entry_number or "")

        layout.addRow("First name:", self.first_name)
        layout.addRow("Last name:", self.last_name)
        layout.addRow("DOB:", self.dob)
        layout.addRow("Entry number:", self.entry_number)

        buttons = QHBoxLayout()
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        buttons.addWidget(save_btn)
        buttons.addWidget(cancel_btn)
        layout.addRow(buttons)

        self.setLayout(layout)

    def get_data(self):
        first = self.first_name.text().strip()
        last = self.last_name.text().strip()
        entry = self.entry_number.text().strip()

        if not last:
            QMessageBox.warning(self, "Validation error", "Last name is required.")
            return None
        if not entry:
            QMessageBox.warning(self, "Validation error", "Entry number is required.")
            return None

        return {
            "FirstName": first,
            "LastName": last,
            "DOB": self.dob.date().toPython(),
            "EntryNumber": entry
        }

class GoatEntryDialog(QDialog):
    """Add/Edit Goat dialog."""

    def __init__(self, parent=None, goat=None):
        super().__init__(parent)
        self.setWindowTitle("Add/Edit Goat")
        layout = QFormLayout()

        self.goat_name = QLineEdit()
        self.breed = QLineEdit()
        self.dob = QDateEdit()
        self.dob.setCalendarPopup(True)
        self.dob.setDate(date.today())

        if goat:
            self.goat_name.setText(goat.name)
            self.breed.setText(goat.breed)
            if goat.dob:
                self.dob.setDate(goat.dob)

        layout.addRow("Goat name:", self.goat_name)
        layout.addRow("Breed:", self.breed)
        layout.addRow("DOB:", self.dob)

        buttons = QHBoxLayout()
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        buttons.addWidget(save_btn)
        buttons.addWidget(cancel_btn)
        layout.addRow(buttons)

        self.setLayout(layout)

    def get_data(self):
        return {
            "Goat": self.goat_name.text().strip(),
            "Breed": self.breed.text().strip(),
            "GoatDOB": self.dob.date().toPython()
        }

class ClassEntryDialog(QDialog):
    """Add/Edit Class Entry dialog with auto payout from awards.xlsx."""

    def __init__(self, parent=None, class_entry=None):
        super().__init__(parent)
        self.setWindowTitle("Add/Edit Class")
        layout = QFormLayout()

        self.class_name = QLineEdit()
        self.show_date = QDateEdit()
        self.show_date.setCalendarPopup(True)
        self.show_date.setDate(date.today())
        self.placement = QLineEdit()
        self.ribbon = QLineEdit()
        self.payout = QDoubleSpinBox()
        self.payout.setMaximum(100000.0)
        self.payout.setPrefix("$")
        self.payout.setDecimals(2)

        if class_entry:
            self.class_name.setText(class_entry.class_name)
            if class_entry.show_date:
                self.show_date.setDate(class_entry.show_date)
            self.placement.setText(class_entry.placement or "")
            self.ribbon.setText(class_entry.ribbon or "")
            self.payout.setValue(class_entry.payout or 0.0)

        layout.addRow("Class name:", self.class_name)
        layout.addRow("Show date:", self.show_date)
        layout.addRow("Placement:", self.placement)
        layout.addRow("Ribbon:", self.ribbon)
        layout.addRow("Payout:", self.payout)

        auto_btn = QPushButton("Auto-calc payout from awards.xlsx")
        auto_btn.clicked.connect(self.auto_calc_payout)
        layout.addRow(auto_btn)

        buttons = QHBoxLayout()
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        buttons.addWidget(save_btn)
        buttons.addWidget(cancel_btn)
        layout.addRow(buttons)

        self.setLayout(layout)

    def auto_calc_payout(self):
        placement = self.placement.text().strip()
        ribbon = self.ribbon.text().strip()
        payout = 0.0
        if placement in PLACEMENT_VALUES:
            payout = PLACEMENT_VALUES[placement]
        elif ribbon in RIBBON_VALUES:
            payout = RIBBON_VALUES[ribbon]
        self.payout.setValue(float(payout))

    def get_data(self):
        return {
            "Class": self.class_name.text().strip(),
            "ShowDate": self.show_date.date().toPython(),
            "Placement": self.placement.text().strip(),
            "Ribbon": self.ribbon.text().strip(),
            "Payout": float(self.payout.value())
        }
# ---------- Main GUI ----------
class GoatShowGUI(QWidget):
    CUSTOM_ROLE = 1000

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goat Show Manager")
        self.exhibitors = []
        self.source_file_path = None

        root = QVBoxLayout()
        root.addWidget(QLabel("Choose how to start:"))

        # Search/filter bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search by last name or entry number…")
        self.search_bar.textChanged.connect(self.apply_filter)
        root.addWidget(self.search_bar)

        # Status label
        self.status_label = QLabel("Showing 0 exhibitors")
        root.addWidget(self.status_label)

        # Top actions
        top_row = QHBoxLayout()
        gui_button = QPushButton("Run GUI Only")
        gui_button.clicked.connect(self.run_gui_only)
        reformatter_button = QPushButton("Run with Reformatter")
        reformatter_button.clicked.connect(self.run_with_reformatter)
        add_exhibitor_button = QPushButton("Add Exhibitor")
        add_exhibitor_button.clicked.connect(self.add_exhibitor)
        reload_awards_button = QPushButton("Reload awards.xlsx")
        reload_awards_button.clicked.connect(self.reload_awards)
        top_row.addWidget(gui_button)
        top_row.addWidget(reformatter_button)
        top_row.addWidget(add_exhibitor_button)
        top_row.addWidget(reload_awards_button)
        root.addLayout(top_row)

        # Secondary actions
        action_row = QHBoxLayout()
        save_button = QPushButton("Save archive to Excel")
        save_button.clicked.connect(self.save_to_excel)
        report_button = QPushButton("Generate payout report")
        report_button.clicked.connect(self.generate_report)
        add_goat_button = QPushButton("Add Goat to selected exhibitor")
        add_goat_button.clicked.connect(self.add_goat_to_selected)
        add_class_button = QPushButton("Add Class to selected exhibitor")
        add_class_button.clicked.connect(self.add_class_to_selected)
        action_row.addWidget(save_button)
        action_row.addWidget(report_button)
        action_row.addWidget(add_goat_button)
        action_row.addWidget(add_class_button)
        root.addLayout(action_row)

        # Exhibitor list
        self.list_widget = QListWidget()
        self.list_widget.itemDoubleClicked.connect(self.edit_item)
        root.addWidget(self.list_widget)

        self.setLayout(root)
    # ---------- Popup helpers ----------
    def show_error(self, message: str):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec()

    def show_info(self, message: str):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Info")
        msg_box.setText(message)
        msg_box.exec()

    # ---------- Search/filter ----------
    def apply_filter(self, text: str):
        """Filter exhibitors by last name or entry number."""
        text = (text or "").strip().lower()
        if not text:
            self.display_exhibitors(self.exhibitors)
            return

        filtered = [
            ex for ex in self.exhibitors
            if text in (ex.last_name or "").lower()
            or text in (ex.entry_number or "").lower()
        ]
        self.display_exhibitors(filtered)

    # ---------- Awards reload ----------
    def reload_awards(self):
        global PLACEMENT_VALUES, RIBBON_VALUES
        PLACEMENT_VALUES, RIBBON_VALUES = load_awards()
        self.show_info("Awards reloaded from data/awards.xlsx")

    # ---------- Display ----------
    def display_exhibitors(self, exhibitors):
        self.list_widget.clear()
        exhibitors_sorted = sorted(exhibitors, key=lambda ex: (ex.last_name or "").lower())

        for exhibitor in exhibitors_sorted:
            dob_str = format_dob(exhibitor.dob)
            age_str = f"{exhibitor.age} years" if exhibitor.age is not None else "—"
            header = (
                f"{exhibitor.last_name}, {exhibitor.first_name} "
                f"(ID: {exhibitor.id}, Entry#: {exhibitor.entry_number}) "
                f"DOB: {dob_str} Age: {age_str}"
            )
            ex_item = QListWidgetItem(header)
            ex_item.setData(self.CUSTOM_ROLE, ("exhibitor", exhibitor))
            self.list_widget.addItem(ex_item)

            for goat in exhibitor.goats:
                goat_line = f"   - Goat: {goat.name} | Breed: {goat.breed} | DOB: {format_dob(goat.dob)}"
                goat_item = QListWidgetItem(goat_line)
                goat_item.setData(self.CUSTOM_ROLE, ("goat", exhibitor, goat))
                self.list_widget.addItem(goat_item)

            for c in exhibitor.classes:
                show_str = format_dob(c.show_date)
                class_line = (
                    f"   * Class: {c.class_name} | Show: {show_str} | "
                    f"Placement: {c.placement or '—'} | Ribbon: {c.ribbon or '—'} | Payout: ${c.payout:.2f}"
                )
                class_item = QListWidgetItem(class_line)
                class_item.setData(self.CUSTOM_ROLE, ("class", exhibitor, c))
                self.list_widget.addItem(class_item)

        # update status label
        self.status_label.setText(f"Showing {len(exhibitors_sorted)} exhibitors")

    # ---------- Editing ----------
    def edit_item(self, item: QListWidgetItem):
        data = item.data(self.CUSTOM_ROLE)
        if not data:
            return

        kind = data[0]
        if kind == "exhibitor":
            exhibitor = data[1]
            dialog = ExhibitorDialog(self, exhibitor)
            if dialog.exec():
                updated = dialog.get_data()
                if not updated:
                    return
                exhibitor.first_name = updated["FirstName"]
                exhibitor.last_name = updated["LastName"]
                exhibitor.dob = updated["DOB"]
                exhibitor.entry_number = updated["EntryNumber"]
                self.display_exhibitors(self.exhibitors)

        elif kind == "goat":
            exhibitor, goat = data[1], data[2]
            dialog = GoatEntryDialog(self, goat)
            if dialog.exec():
                updated = dialog.get_data()
                goat.name = updated["Goat"]
                goat.breed = updated["Breed"]
                goat.dob = updated["GoatDOB"]
                self.display_exhibitors(self.exhibitors)

        elif kind == "class":
            exhibitor, class_entry = data[1], data[2]
            dialog = ClassEntryDialog(self, class_entry)
            if dialog.exec():
                updated = dialog.get_data()
                class_entry.class_name = updated["Class"]
                class_entry.show_date = updated["ShowDate"]
                class_entry.placement = updated["Placement"]
                class_entry.ribbon = updated["Ribbon"]
                class_entry.payout = updated["Payout"]
                self.display_exhibitors(self.exhibitors)

    # ---------- Add workflows ----------
    def add_exhibitor(self):
        dialog = ExhibitorDialog(self)
        if dialog.exec():
            data = dialog.get_data()
            if not data:
                return
            new_id = (max([ex.id for ex in self.exhibitors], default=0) + 1)
            exhibitor = Exhibitor(
                id=new_id,
                first_name=data["FirstName"],
                last_name=data["LastName"],
                dob=data["DOB"],
                entry_number=data["EntryNumber"],
                goats=[],
                classes=[]
            )
            self.exhibitors.append(exhibitor)
            self.display_exhibitors(self.exhibitors)

    def add_goat_to_selected(self):
        item = self.list_widget.currentItem()
        if not item:
            self.show_error("Select an exhibitor first.")
            return
        data = item.data(self.CUSTOM_ROLE)
        if not data or data[0] != "exhibitor":
            self.show_error("Select an exhibitor header line to add a goat.")
            return
        exhibitor = data[1]
        dialog = GoatEntryDialog(self)
        if dialog.exec():
            d = dialog.get_data()
            new_goat = Goat(
                id=(max([g.id for g in exhibitor.goats], default=0) + 1),
                name=d["Goat"],
                breed=d["Breed"],
                dob=d["GoatDOB"],
                exhibitor_id=exhibitor.id
            )
            exhibitor.goats.append(new_goat)
            self.display_exhibitors(self.exhibitors)

    def add_class_to_selected(self):
        item = self.list_widget.currentItem()
        if not item:
            self.show_error("Select an exhibitor first.")
            return
        data = item.data(self.CUSTOM_ROLE)
        if not data or data[0] != "exhibitor":
            self.show_error("Select an exhibitor header line to add a class.")
            return
        exhibitor = data[1]
        dialog = ClassEntryDialog(self)
        if dialog.exec():
            d = dialog.get_data()
            new_class = ClassEntry(
                id=(max([c.id for c in exhibitor.classes], default=0) + 1),
                exhibitor_id=exhibitor.id,
                exhibitor_name=f"{exhibitor.first_name} {exhibitor.last_name}",
                class_name=d["Class"],
                show_date=d["ShowDate"],
                placement=d["Placement"],
                ribbon=d["Ribbon"],
                payout=d["Payout"]
            )
            exhibitor.classes.append(new_class)
            self.display_exhibitors(self.exhibitors)

    # ---------- Save archive ----------
    def save_to_excel(self):
        if not self.exhibitors:
            self.show_error("No data to save.")
            return

        output_file, _ = QFileDialog.getSaveFileName(self, "Save show archive", "", "Excel Files (*.xlsx)")
        if not output_file:
            return

        exhibitor_rows, goat_rows, class_rows = [], [], []
        for ex in self.exhibitors:
            exhibitor_rows.append({
                "ExhibitorID": ex.id,
                "FirstName": ex.first_name,
                "LastName": ex.last_name,
                "ExhibitorDOB": ex.dob,
                "EntryNumber": ex.entry_number
            })
            for g in ex.goats:
                goat_rows.append({
                    "ExhibitorID": ex.id,
                    "GoatID": g.id,
                    "Goat": g.name,
                    "Breed": g.breed,
                    "GoatDOB": g.dob
                })
            for c in ex.classes:
                class_rows.append({
                    "ExhibitorID": ex.id,
                    "Class": c.class_name,
                    "ShowDate": c.show_date,
                    "Placement": c.placement,
                    "Ribbon": c.ribbon,
                    "Payout": c.payout
                })

        df_exhibitors = pd.DataFrame(exhibitor_rows)
        df_goats = pd.DataFrame(goat_rows)
        df_classes = pd.DataFrame(class_rows)

        totals = pd.DataFrame()
        if not df_classes.empty:
            totals = df_classes.groupby(["ExhibitorID"])["Payout"].sum().reset_index()
            totals.rename(columns={"Payout": "ExhibitorTotal"}, inplace=True)
            grand_total = totals["ExhibitorTotal"].sum()
            totals["GrandTotalAllExhibitors"] = grand_total

        try:
            with pd.ExcelWriter(output_file) as writer:
                df_exhibitors.to_excel(writer, sheet_name="Exhibitors", index=False)
                df_goats.to_excel(writer, sheet_name="Goats", index=False)
                df_classes.to_excel(writer, sheet_name="Classes", index=False)
                if not totals.empty:
                    totals.to_excel(writer, sheet_name="Totals", index=False)
            self.show_info(f"Archive saved to:\n{output_file}")
        except PermissionError:
            self.show_error("Permission denied. Close the file if it's already open in Excel.")
        except Exception as e:
            self.show_error(f"Failed to save archive:\n{e}")

    # ---------- Generate payout report ----------
    def generate_report(self):
        if not self.exhibitors:
            self.show_error("No data to report.")
            return

        output_file, _ = QFileDialog.getSaveFileName(self, "Save payout report", "", "Excel Files (*.xlsx)")
        if not output_file:
            return

        try:
            generate_payout_report(self.exhibitors, output_file)
            self.show_info(f"Payout report saved to:\n{output_file}")
        except PermissionError:
            self.show_error("Permission denied. Close the file if it's already open in Excel.")
        except Exception as e:
            self.show_error(f"Failed to generate report:\n{e}")

    # ---------- Load workflows ----------
    def run_gui_only(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel file", "", "Excel Files (*.xlsx)")
        if file_path:
            try:
                df = pd.read_excel(file_path)
                self.source_file_path = file_path
                self.exhibitors = self.build_models(df)
                self.display_exhibitors(self.exhibitors)
                self.show_info("File loaded successfully.")
            except FileNotFoundError:
                self.show_error("The selected file could not be found.")
            except ValueError as ve:
                self.show_error(f"Data format error:\n{ve}")
            except Exception as e:
                self.show_error(f"Unexpected error:\n{e}")

    def run_with_reformatter(self):
        input_file, _ = QFileDialog.getOpenFileName(self, "Select input Excel file", "", "Excel Files (*.xlsx)")
        if input_file:
            output_file, _ = QFileDialog.getSaveFileName(self, "Save reformatted file", "", "Excel Files (*.xlsx)")
            if output_file:
                try:
                    formatted = reformat_excel(input_file, output_file)
                    df = pd.read_excel(formatted)
                    self.source_file_path = formatted
                    validate_columns(df)
                    self.exhibitors = self.build_models(df)
                    self.display_exhibitors(self.exhibitors)
                    self.show_info("File reformatted and loaded successfully.")
                except FileNotFoundError:
                    self.show_error("Input file not found.")
                except PermissionError:
                    self.show_error("Permission denied. Close the output file if it's open in Excel.")
                except ValueError as ve:
                    self.show_error(f"Data format error:\n{ve}")
                except Exception as e:
                    self.show_error(f"Reformatter failed:\n{e}")


# ---------- Entry point ----------
def run_gui():
    app = QApplication(sys.argv)
    window = GoatShowGUI()
    window.show()
    sys.exit(app.exec())
