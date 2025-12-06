# Goat Show Manager Data Model 🐐

This document defines the core data models used in Goat Show Manager.  
Each model represents a key entity in the system and is designed for clarity, scalability, and testability.

---

## 🐐 Goat
Represents an individual goat entered into a show.

**Attributes:**
- `id` (int): Unique identifier
- `name` (str): Goat’s name
- `breed` (str): Breed type
- `age` (int): Age in years
- `owner_id` (int): Foreign key linking to Owner

---

## 👤 Owner
Represents the person responsible for one or more goats.

**Attributes:**
- `id` (int): Unique identifier
- `name` (str): Owner’s full name
- `contact_info` (str): Email or phone number
- `goats` (list[int]): IDs of goats owned

---

## 🎪 Show
Represents a goat show event.

**Attributes:**
- `id` (int): Unique identifier
- `date` (date): Date of the show
- `location` (str): Venue or city
- `participants` (list[int]): Goat IDs registered
- `judges` (list[int]): Judge IDs assigned
- `results` (dict): Mapping of goat IDs to scores/rankings

---

## ⚖️ Judge
Represents a judge who evaluates goats in a show.

**Attributes:**
- `id` (int): Unique identifier
- `name` (str): Judge’s full name
- `criteria` (list[str]): Evaluation criteria (e.g., breed standard, presentation, health)

---

## 🔗 Relationships
- **Owner ↔ Goat**: One owner can have multiple goats.
- **Show ↔ Goat**: A show can have many goats registered.
- **Show ↔ Judge**: A show can have multiple judges.
- **Results**: Stored in the Show model, linking goats to scores.

---

## 🧪 Example (Python Dataclasses)
```python
from dataclasses import dataclass
from datetime import date
from typing import List, Dict

@dataclass
class Goat:
    id: int
    name: str
    breed: str
    age: int
    owner_id: int

@dataclass
class Owner:
    id: int
    name: str
    contact_info: str
    goats: List[int]

@dataclass
class Show:
    id: int
    date: date
    location: str
    participants: List[int]
    judges: List[int]
    results: Dict[int, int]  # goat_id -> score

@dataclass
class Judge:
    id: int
    name: str
    criteria: List[str]

📜 Notes
IDs can be integers or UUIDs depending on future database integration.

Relationships are currently represented by IDs; later, ORM (e.g., SQLAlchemy) can replace them with direct object references.

Results are flexible: can store scores, rankings, or detailed feedback.

