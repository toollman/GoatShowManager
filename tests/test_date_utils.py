import pytest
from datetime import date
from src.utils.date_utils import parse_dob, format_dob, calculate_age

def test_parse_dob_iso_format():
    dob = parse_dob("2020-01-15")
    assert dob == date(2020, 1, 15)

def test_parse_dob_us_format():
    dob = parse_dob("01/15/2020")
    assert dob == date(2020, 1, 15)

def test_parse_dob_invalid():
    dob = parse_dob("not-a-date")
    assert dob is None

def test_format_dob_known():
    dob = date(1980, 5, 12)
    assert format_dob(dob) == "05/12/1980"

def test_format_dob_unknown():
    assert format_dob(None) == "Unknown"

def test_calculate_age_known():
    dob = date(2000, 12, 1)
    age = calculate_age(dob)
    today = date.today()
    expected_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    assert age == expected_age

def test_calculate_age_unknown():
    assert calculate_age(None) == 0
