# Goat Show Manager Workflow 🐐

This document describes the core user workflows for Goat Show Manager.  
It explains how users interact with the system to register goats, schedule shows, and record results.

---

## 🎯 Goals
- Provide clear, step-by-step processes for common tasks
- Align workflows with the data models and architecture
- Ensure consistency between CLI, services, and models
- Support future extensions (web UI, database integration)

---

## 🐐 Workflow 1: Registering a Goat
1. User selects **"Register Goat"** from the CLI menu.
2. System prompts for goat details:
   - Name
   - Breed
   - Age
   - Owner ID (or create new Owner if not found)
3. Goat object is created in `models/Goat`.
4. Goat is added to the owner’s list of goats.
5. Confirmation message is displayed.

---

## 🎪 Workflow 2: Scheduling a Show
1. User selects **"Create Show"** from the CLI menu.
2. System prompts for show details:
   - Date
   - Location
3. Show object is created in `models/Show`.
4. Show is added to the list of upcoming events.
5. Confirmation message is displayed.

---

## 📝 Workflow 3: Registering Goats for a Show
1. User selects **"Add Goat to Show"** from the CLI menu.
2. System prompts for:
   - Show ID
   - Goat ID
3. Goat ID is added to the show’s `participants` list.
4. Confirmation message is displayed.

---

## ⚖️ Workflow 4: Assigning Judges
1. User selects **"Assign Judge"** from the CLI menu.
2. System prompts for:
   - Show ID
   - Judge details (name, criteria)
3. Judge object is created in `models/Judge`.
4. Judge ID is added to the show’s `judges` list.
5. Confirmation message is displayed.

---

## 🏆 Workflow 5: Recording Results
1. User selects **"Record Results"** from the CLI menu.
2. System prompts for:
   - Show ID
   - Goat ID
   - Score or ranking
3. Entry is added to the show’s `results` dictionary.
4. Confirmation message is displayed.
5. Results can be exported via `utils` (CSV/JSON).

---

## 🔗 Workflow Relationships
- **Register Goat** → feeds into **Registering Goats for a Show**
- **Create Show** → feeds into **Assigning Judges** and **Registering Goats**
- **Record Results** → depends on goats and judges being assigned

---

## 📜 Future Extensions
- **Web UI:** Replace CLI prompts with forms and dashboards
- **Database:** Persist goats, owners, shows, and results in SQLite/PostgreSQL
- **Analytics:** Generate reports on goat performance, owner participation, and judge scoring trends
