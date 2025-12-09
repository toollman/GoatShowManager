import pytest
import pandas as pd
from src.reformatter_core import validate_columns, reformat_excel

def test_validate_columns_missing_goatdob():
    df = pd.DataFrame({
        "ExhibitorID": [1],
        "Exhibitor": ["Alice"],
        "ExhibitorDOB": ["1980-05-12"],
        "GoatID": [101],
        "Goat": ["Daisy"],
        # GoatDOB missing
        "Breed": ["Nubian"],
        "Payout": [100.0]
    })
    with pytest.raises(ValueError) as excinfo:
        validate_columns(df)
    assert "GoatDOB" in str(excinfo.value)

def test_validate_columns_success(tmp_path):
    df = pd.DataFrame({
        "ExhibitorID": [1],
        "Exhibitor": ["Alice"],
        "ExhibitorDOB": ["1980-05-12"],
        "GoatID": [101],
        "Goat": ["Daisy"],
        "GoatDOB": ["2020-01-15"],
        "Breed": ["Nubian"],
        "Payout": [100.0]
    })
    # Should not raise
    validate_columns(df)

    # Test reformat_excel saves cleaned file
    input_file = tmp_path / "input.xlsx"
    output_file = tmp_path / "output.xlsx"
    df.to_excel(input_file, index=False)
    result = reformat_excel(str(input_file), str(output_file))
    assert result == str(output_file)
