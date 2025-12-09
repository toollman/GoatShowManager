from datetime import date
from src.models.goat import Goat
from src.models.exhibitor import Exhibitor

def test_goat_age_calculation():
    dob = date(2020, 1, 15)
    goat = Goat(id=1, name="Daisy", breed="Nubian", dob=dob, exhibitor_id=101)
    today = date.today()
    expected_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    assert goat.age == expected_age

def test_exhibitor_age_calculation():
    dob = date(1980, 5, 12)
    exhibitor = Exhibitor(id=101, name="Alice Johnson", dob=dob, goats=[])
    today = date.today()
    expected_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    assert exhibitor.age == expected_age
