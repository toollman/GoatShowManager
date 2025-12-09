import pandas as pd

REQUIRED_COLUMNS = [
    "ExhibitorID",
    "Exhibitor",
    "ExhibitorDOB",
    "GoatID",
    "Goat",
    "GoatDOB",
    "Breed",
    "Payout"
]

def validate_columns(df: pd.DataFrame):
    """Ensure all required columns exist in the Excel file."""
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(
            f"Missing required columns: {', '.join(missing)}.\n"
            f"Expected columns: {', '.join(REQUIRED_COLUMNS)}"
        )

def reformat_excel(input_file: str, output_file: str) -> str:
    """
    Load Excel, validate required columns, and save a cleaned version.
    Returns path to the reformatted file.
    """
    df = pd.read_excel(input_file)

    # Validate structure
    validate_columns(df)

    # Example cleanup: strip whitespace from exhibitor names
    df["Exhibitor"] = df["Exhibitor"].str.strip()

    # Save cleaned file
    df.to_excel(output_file, index=False)
    return output_file
