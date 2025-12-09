import pandas as pd
from src.reports.report_generator import generate_report

def test_generate_report_with_class_subtotals(tmp_path):
    df = pd.DataFrame({
        "ExhibitorID": [1, 1, 2],
        "Exhibitor": ["Alice", "Alice", "Bob"],
        "ExhibitorDOB": ["1980-05-12", "1980-05-12", "1975-11-02"],
        "Class": ["Junior Doe", "Senior Doe", "Market Goat"],
        "ShowDate": ["2023-06-01", "2023-06-01", "2023-06-02"],
        "Payout": [100.0, 150.0, 200.0]
    })

    input_file = tmp_path / "input.xlsx"
    output_file = tmp_path / "report.xlsx"
    df.to_excel(input_file, index=False)

    result = generate_report(str(input_file), str(output_file))
    assert result == str(output_file)

    class_subtotals = pd.read_excel(output_file, sheet_name="Class Subtotals")
    exhibitor_totals = pd.read_excel(output_file, sheet_name="Exhibitor Totals")

    # Check class subtotals
    assert class_subtotals.loc[class_subtotals["Class"] == "Junior Doe", "ClassSubtotal"].iloc[0] == 100.0
    assert class_subtotals.loc[class_subtotals["Class"] == "Senior Doe", "ClassSubtotal"].iloc[0] == 150.0
    assert class_subtotals.loc[class_subtotals["Class"] == "Market Goat", "ClassSubtotal"].iloc[0] == 200.0

    # Check exhibitor totals
    assert exhibitor_totals.loc[exhibitor_totals["Exhibitor"] == "Alice", "ExhibitorTotal"].iloc[0] == 250.0
    assert exhibitor_totals.loc[exhibitor_totals["Exhibitor"] == "Bob", "ExhibitorTotal"].iloc[0] == 200.0
    assert exhibitor_totals["GrandTotalAllExhibitors"].iloc[0] == 450.0
