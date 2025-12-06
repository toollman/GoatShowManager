from src.models import Goat, Owner, Show

# Temporary in-memory storage (replace later with DB or file I/O)
goats = {}
owners = {}
shows = {}

def register_owner(name: str, contact: str) -> Owner:
    owner_id = len(owners) + 1
    owner = Owner(id=owner_id, name=name, contact_info=contact, goats=[])
    owners[owner_id] = owner
    return owner

def register_goat(name: str, breed: str, age: int, owner_id: int) -> Goat:
    if owner_id not in owners:
        raise ValueError("Owner ID not found")
    goat_id = len(goats) + 1
    goat = Goat(id=goat_id, name=name, breed=breed, age=age, owner_id=owner_id)
    goats[goat_id] = goat
    owners[owner_id].goats.append(goat_id)
    return goat

def add_goat_to_show(show_id: int, goat_id: int) -> None:
    if show_id not in shows or goat_id not in goats:
        raise ValueError("Invalid show or goat ID")
    shows[show_id].participants.append(goat_id)
