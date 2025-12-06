import sys
from src.models import Goat, Owner, Show, Judge

# Temporary in-memory storage (replace later with database or file I/O)
goats = {}
owners = {}
shows = {}
judges = {}

def register_goat():
    name = input("Enter goat name: ")
    breed = input("Enter breed: ")
    age = int(input("Enter age: "))
    owner_id = int(input("Enter owner ID (or 0 to create new): "))

    if owner_id == 0:
        owner_name = input("Enter owner name: ")
        contact = input("Enter owner contact info: ")
        owner_id = len(owners) + 1
        owners[owner_id] = Owner(id=owner_id, name=owner_name, contact_info=contact, goats=[])

    goat_id = len(goats) + 1
    goat = Goat(id=goat_id, name=name, breed=breed, age=age, owner_id=owner_id)
    goats[goat_id] = goat
    owners[owner_id].goats.append(goat_id)

    print(f"✅ Goat '{name}' registered with ID {goat_id}.")

def create_show():
    date = input("Enter show date (YYYY-MM-DD): ")
    location = input("Enter show location: ")
    show_id = len(shows) + 1
    shows[show_id] = Show(id=show_id, date=date, location=location,
                          participants=[], judges=[], results={})
    print(f"✅ Show created with ID {show_id}.")

def add_goat_to_show():
    show_id = int(input("Enter show ID: "))
    goat_id = int(input("Enter goat ID: "))
    if show_id in shows and goat_id in goats:
        shows[show_id].participants.append(goat_id)
        print(f"✅ Goat {goat_id} added to Show {show_id}.")
    else:
        print("❌ Invalid show or goat ID.")

def assign_judge():
    show_id = int(input("Enter show ID: "))
    name = input("Enter judge name: ")
    criteria = input("Enter evaluation criteria (comma-separated): ").split(",")
    judge_id = len(judges) + 1
    judges[judge_id] = Judge(id=judge_id, name=name, criteria=criteria)
    shows[show_id].judges.append(judge_id)
    print(f"✅ Judge '{name}' assigned to Show {show_id}.")

def record_results():
    show_id = int(input("Enter show ID: "))
    goat_id = int(input("Enter goat ID: "))
    score = int(input("Enter score: "))
    if show_id in shows and goat_id in goats:
        shows[show_id].results[goat_id] = score
        print(f"✅ Result recorded: Goat {goat_id} scored {score} in Show {show_id}.")
    else:
        print("❌ Invalid show or goat ID.")

def menu():
    while True:
        print("\n🐐 Goat Show Manager Menu")
        print("1. Register Goat")
        print("2. Create Show")
        print("3. Add Goat to Show")
        print("4. Assign Judge")
        print("5. Record Results")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            register_goat()
        elif choice == "2":
            create_show()
        elif choice == "3":
            add_goat_to_show()
        elif choice == "4":
            assign_judge()
        elif choice == "5":
            record_results()
        elif choice == "6":
            print("👋 Exiting Goat Show Manager.")
            sys.exit()
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
