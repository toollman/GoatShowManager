from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional
from src.utils.date_utils import calculate_age, format_dob
from src.models.goat import Goat
from src.models.class_entry import ClassEntry

@dataclass
class Exhibitor:
    id: int
    first_name: str
    last_name: str
    dob: Optional[date] = None
    goats: List[Goat] = field(default_factory=list)
    classes: List[ClassEntry] = field(default_factory=list)
    entry_number: str = ""   # manually entered show entry number

    @property
    def name(self) -> str:
        """Full name convenience property."""
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self) -> Optional[int]:
        if self.dob:
            return calculate_age(self.dob)
        return None

    @property
    def dob_str(self) -> str:
        return format_dob(self.dob)

    def add_goat(self, goat: Goat):
        self.goats.append(goat)

    def add_class(self, class_entry: ClassEntry):
        self.classes.append(class_entry)
