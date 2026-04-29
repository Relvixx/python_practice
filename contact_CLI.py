import os

# 1. Setup: Load existing data or start fresh
FILE_NAME = "contacts.txt"
contacts = []

# Load data from file if it exists
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        for line in file:
            # Each line is "Name:Phone", so we split it
            name, phone = line.strip().split(":")
            contacts.append({"name": name, "phone": phone})

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Save & Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        # ADD CONTACT
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        # Create a dictionary and add to our list
        contacts.append({"name": name, "phone": phone})
        print(f"Contact for {name} added!")

    elif choice == "2":
        # SEARCH CONTACT
        search_name = input("Who are you looking for? ")
        found = False
        for person in contacts:
            if person["name"].lower() == search_name.lower():
                print(f"Found: {person['name']} - {person['phone']}")
                found = True
                break
        if not found:
            print("Contact not found.")

    elif choice == "3":
        # DELETE CONTACT
        del_name = input("Enter name to delete: ")
        # We create a new list excluding the person we want to delete
        original_count = len(contacts)
        contacts = [p for p in contacts if p["name"].lower() != del_name.lower()]
        
        if len(contacts) < original_count:
            print(f"Deleted {del_name}.")
        else:
            print("No contact found with that name.")

    elif choice == "4":
        # SAVE AND EXIT (File I/O)
        with open(FILE_NAME, "w") as file:
            for person in contacts:
                file.write(f"{person['name']}:{person['phone']}\n")
        print("Contacts saved to contacts.txt. Goodbye!")
        break

    else:
        print("Invalid choice, try again.")