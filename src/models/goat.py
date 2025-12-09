from dataclasses import dataclass
from datetime import date
from src.utils.date_utils import calculate_age

@dataclass
class Goat:
    id: int
    name: str
    breed: str
    dob: date
    exhibitor_id: int

    @property
    def age(self) -> int:
        return calculate_age(self.dob)
