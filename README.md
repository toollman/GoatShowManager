# 🐐 Goat Show Manager

Goat Show Manager is a Python-based application designed to help organize, track, and manage goat shows.  
It provides tools for recording participants, scheduling events, and generating results in a clear, structured way.

---

## Branch Convention
The default branch for this repository is **`main`**.  
All development and pull requests should target `main`.

---

## 🚀 Features
- Manage exhibitors, goats, and class entries
- Track event schedules and results
- Export archives and generate payout reports
- GUI built with PySide6 for accessibility
- Contributor-friendly structure and documentation

---

## 📂 Project Structure
GoatShowManager/

│── .gitignore
│── README.md
│── requirements.txt
│── src/
│ ├── main.py
│ ├── gui/
│ │ └── main.py
│ ├── models/
│ ├── utils/
│── tests/
│ └── test_main.py
│── docs/

---

## ⚙️ Installation

1. Clone the repository:
- git clone https://github.com/your-username/GoatShowManager.git
- cd GoatShowManager
2. Create a virtual environment:
- -python -m venv venv
- -source venv/bin/activate   # Mac/Linux
- -venv\Scripts\activate      # Windows
3. Install dependencies:
- pip install -r requirements.txt

---

▶️ Usage
Run the application:
    python src/main.py
This will launch the Goat Show Manager GUI.

---

🧪 Testing
Run unit tests with:
    pytest

📖 Quick Start for Show Officials
1. Launch the GUI
- Run python src/main.py to open the application.
2. Add Exhibitors
- Click Add Exhibitor.
- Enter first/last name, DOB, and entry number.
- Save to see them listed.
3. Add Goats
- Select an exhibitor in the list.
- Click Add Goat.
- Enter goat name, breed, and DOB.
4. Add Classes
- Select an exhibitor.
- Click Add Class.
- Enter class name, show date, placement, ribbon, and payout.
5. Search & Filter
- Use the search bar to filter exhibitors by last name or entry number.
- Status label updates with the number of exhibitors shown.
6. Save Archive
- Click Save Archive to export exhibitors, goats, and classes to Excel.
- Includes subtotals and grand totals.
7. Generate Payout Report
- Click Generate Report to create a ledger-style payout sheet.
- Sorted by exhibitor last name, with signature lines and grand totals.
8. Reload Awards
- Click Reload Awards to refresh placement and ribbon values from data/awards.xlsx.

---

🤝 Contributing

Use atomic commits with clear messages.

Target all pull requests to main.

Follow GUI-based workflows for accessibility.

See requirements.txt for annotated dependencies.

---

📜 License

This project is licensed under the MIT License. See LICENSE for details.