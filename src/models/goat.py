from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Goat:
    id: int
    name: str
    breed: str
    date_of_birth: date
    owner_id: int
    registration_number: Optional[str] = None
