from datetime import datetime, date
from typing import Optional

def parse_dob(dob_str: str) -> Optional[date]:
    """
    Parse a DOB string into a date object.
    Expects formats like 'YYYY-MM-DD' or 'MM/DD/YYYY'.
    Returns None if parsing fails or input is empty.
    """
    if not dob_str or dob_str.strip() == "":
        return None

    # Try ISO format first (YYYY-MM-DD)
    try:
        return datetime.strptime(dob_str, "%Y-%m-%d").date()
    except ValueError:
        pass

    # Try US format (MM/DD/YYYY)
    try:
        return datetime.strptime(dob_str, "%m/%d/%Y").date()
    except ValueError:
        pass

    # Could add more formats if needed
    return None


def format_dob(dob: Optional[date]) -> str:
    """
    Format a date object into MM/DD/YYYY string.
    Returns 'Unknown' if dob is None.
    """
    if not dob:
        return "Unknown"
    return dob.strftime("%m/%d/%Y")


def calculate_age(dob: Optional[date]) -> int:
    """
    Calculate age in years from DOB.
    Returns 0 if dob is None.
    """
    if not dob:
        return 0
    today = date.today()
    return today.year - dob.year - (
        (today.month, today.day) < (dob.month, dob.day)
    )
