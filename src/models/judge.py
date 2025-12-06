from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Judge:
    id: int
    name: str
    credentials: Optional[str] = None
    contact_info: Optional[str] = None
    shows: List[int] = field(default_factory=list)  # store show IDs
