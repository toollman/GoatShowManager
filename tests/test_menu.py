import pytest
import sys
from src.cli import menu

def test_menu_exit(monkeypatch, capsys):
    # Simulate user entering "6" to exit immediately
    inputs = iter(["6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(SystemExit):
        menu.menu()

    captured = capsys.readouterr()
    assert "Exiting Goat Show Manager" in captured.out

def test_invalid_choice(monkeypatch, capsys):
    # Simulate user entering an invalid option, then "6" to exit
    inputs = iter(["99", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(SystemExit):
        menu.menu()

    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out

def test_register_goat(monkeypatch, capsys):
    # Simulate user inputs for goat registration
    inputs = iter([
        "Daisy",        # goat name
        "Nubian",       # breed
        "3",            # age
        "0",            # owner ID (create new)
        "Alice Farmer", # owner name
        "alice@example.com"  # owner contact
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Monkeypatch Goat and Owner classes to simple stand-ins
    class FakeGoat:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class FakeOwner:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
            self.goats = []

    monkeypatch.setattr(menu, "Goat", FakeGoat)
    monkeypatch.setattr(menu, "Owner", FakeOwner)

    # Run the function
    menu.register_goat()

    captured = capsys.readouterr()
    assert "Goat 'Daisy' registered" in captured.out

    # Verify goat and owner were stored
    assert 1 in menu.goats
    assert menu.goats[1].name == "Daisy"
    assert 1 in menu.owners
    assert menu.owners[1].name == "Alice Farmer"
    assert menu.owners[1].goats == [1]