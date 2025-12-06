# Goat Show Manager Dependencies 🐐

This document explains the purpose of each dependency listed in `requirements.txt`.  
It helps contributors understand why libraries are included and when they are used.

---

## Core Application Dependencies
*(already documented above)*

## Testing and Quality Assurance
*(already documented above)*

## Reporting and Export
*(already documented above)*

---

## Future Dependencies (Planned Roadmap)

These libraries are not yet required, but may be added as Goat Show Manager grows.

### GUI Frameworks
- **Tkinter (built-in)**  
  Python’s standard GUI library. Lightweight, easy to use, and good for simple forms and menus.  
  Likely first choice for building the initial graphical interface.

- **PyQt6 / PySide6**  
  More advanced GUI frameworks with modern widgets, styling, and cross‑platform support.  
  Useful if Goat Show Manager needs a polished, professional desktop application.

- **Flask / FastAPI**  
  Web frameworks for building browser‑based interfaces or APIs.  
  Could be used if Goat Show Manager evolves into a web app with online access.

### Database / Persistence
- **SQLite (built-in)**  
  Lightweight relational database included with Python.  
  Ideal for storing goats, owners, shows, and results locally without extra setup.

- **SQLAlchemy**  
  ORM (Object Relational Mapper) that simplifies database interactions.  
  Provides a clean way to map Goat Show Manager’s models to database tables.

- **PostgreSQL / MySQL**  
  Full‑scale relational databases.  
  Useful if Goat Show Manager needs to scale for larger events or multi‑user environments.

### Reporting / Visualization
- **matplotlib / seaborn**  
  Libraries for charts and graphs.  
  Could be used to visualize scores, participation trends, or show statistics.

- **reportlab**  
  Advanced PDF generation library.  
  Useful for creating polished exhibitor reports with logos, tables, and styled layouts.

---

## Notes
- Dependencies will be added incrementally as features are implemented.  
- Contributors should check `requirements.txt` before installing new libraries.  
- This roadmap ensures Goat Show Manager remains modular and future‑proof.
