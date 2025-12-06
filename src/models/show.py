from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List

@dataclass
class Show:
    id: int
    name: str
    location: str
    date: date
    description: Optional[str] = None
    goat_ids: List[int] = field(default_factory=list)
    judge_ids: List[int] = field(default_factory=list)
