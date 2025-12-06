# Goat Show Manager Architecture 🐐

This document outlines the system architecture for Goat Show Manager.  
It describes the core modules, their responsibilities, and how they interact.

---

## 🎯 Goals
- Provide a modular, maintainable codebase
- Separate concerns (data, logic, utilities, UI/CLI)
- Support testing and scalability
- Enable future extensions (databases, reporting, analytics)

---

## 📂 Project Structure
GoatShowManager/
 │── src/ │
 ├── main.py # Entry point
 │ ├── models/ # Data models (Goat, Owner, Show, Judge)
 │ ├── services/ # Business logic (registration, scoring, scheduling)
 │ ├── utils/ # Helper functions (validation, formatting, file I/O)
 │ ├── cli/ # Command-line interface (menus, user input)
 │── tests/ # Unit tests
 │── docs/ # Documentation


---

## 🧩 Core Modules

### 1. `main.py`
- Entry point of the application
- Initializes services and CLI
- Coordinates high-level workflow

### 2. `models/`
- Defines core data structures:
  - `Goat` (id, name, breed, age, owner)
  - `Owner` (id, name, contact info)
  - `Show` (id, date, location, participants)
  - `Judge` (id, name, criteria)
- Uses Python classes or dataclasses for clarity

### 3. `services/`
- Implements business logic:
  - Registration of goats into shows
  - Scoring and ranking
  - Scheduling events
- Acts as the “engine” of the system

### 4. `utils/`
- Provides reusable helpers:
  - Input validation
  - Data formatting
  - File I/O (CSV, JSON export)

### 5. `cli/`
- Handles user interaction via command line
- Provides menus and prompts
- Calls services to perform actions

---

## 🔗 Module Interactions
- **CLI → Services → Models**  
  User input flows from CLI into services, which manipulate models.
- **Services → Utils**  
  Services rely on utilities for validation and formatting.
- **Tests → All Modules**  
  Unit tests cover models, services, and utilities.

---

## 🧪 Testing Strategy
- Use `pytest` for unit tests
- Organize tests by module:
  - `tests/test_models.py`
  - `tests/test_services.py`
  - `tests/test_utils.py`
- Aim for high coverage of business logic

---

## 📜 Future Extensions
- **Database Integration:** Replace file-based storage with SQLite or PostgreSQL
- **Web Interface:** Add a Flask/Django frontend
- **Analytics:** Generate reports and visualizations
- **AI Features:** Use ML models for predictive scoring or breed classification
