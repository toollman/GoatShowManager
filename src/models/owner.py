from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Owner:
    id: int
    name: str
    contact_info: str
    farm_name: Optional[str] = None
    goats: List[int] = field(default_factory=list)  # store goat IDs
