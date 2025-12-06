import pytest
from datetime import date
from src.models import Goat, Owner, Show, Judge

def test_goat_creation():
    goat = Goat(
        id=1,
        name="Daisy",
        breed="Nubian",
        date_of_birth=date(2020, 5, 14),
        owner_id=101,
        registration_number="REG123"
    )
    assert goat.name == "Daisy"
    assert goat.breed == "Nubian"
    assert goat.owner_id == 101

def test_owner_creation():
    owner = Owner(
        id=101,
        name="Alice Farmer",
        contact_info="alice@example.com",
        farm_name="Sunny Acres"
    )
    assert owner.name == "Alice Farmer"
    assert owner.farm_name == "Sunny Acres"
    assert owner.goats == []  # default empty list

def test_show_creation():
    show = Show(
        id=201,
        name="Spring Goat Show",
        location="Green Cove Springs Fairgrounds",
        date=date(2025, 4, 20),
        description="Annual spring event"
    )
    assert show.name == "Spring Goat Show"
    assert show.location == "Green Cove Springs Fairgrounds"
    assert show.goat_ids == []
    assert show.judge_ids == []

def test_judge_creation():
    judge = Judge(
        id=301,
        name="Bob Judge",
        credentials="Certified Goat Judge",
        contact_info="bob@example.com"
    )
    assert judge.name == "Bob Judge"
    assert judge.credentials == "Certified Goat Judge"
    assert judge.shows == []
