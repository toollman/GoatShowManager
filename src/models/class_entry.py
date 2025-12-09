from dataclasses import dataclass
from datetime import date
from src.utils.date_utils import format_dob

@dataclass
class ClassEntry:
    id: int
    exhibitor_id: int
    exhibitor_name: str
    class_name: str
    show_date: date
    payout: float = 0.0
    placement: str = ""   # e.g. "1st", "2nd", "Grand Champion"
    ribbon: str = ""      # e.g. "Blue", "Red", "White", "Green"

    @property
    def show_date_str(self) -> str:
        return format_dob(self.show_date)
