import pytest
from src import main

def test_main_prints_welcome_message(capsys, monkeypatch):
    # Monkeypatch menu() so it doesn't actually run the CLI loop
    monkeypatch.setattr("src.cli.menu.menu", lambda: None)

    main.main()  # run the entry point

    captured = capsys.readouterr()
    assert "🐐 Welcome to Goat Show Manager" in captured.out

def test_main_calls_menu(monkeypatch):
    called = {}

    def fake_menu():
        called["menu"] = True

    monkeypatch.setattr("src.cli.menu.menu", fake_menu)

    main.main()
    assert called.get("menu") is True
