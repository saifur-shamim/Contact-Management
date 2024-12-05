import os, adding, saving,removing, searching

contact_list = []
nums_collection = set()

# Function to find previous loaded contacts from the file

def load_contacts():
    if os.path.exists("list.csv"):
        with open("list.csv", "r") as fp:
            for line in fp:
                name, phone, email, address = line.strip().split(", ")
                phone = int(phone)
                contact = adding.Contact(name, phone, email, address)
                contact_list.append(contact)
                nums_collection.add(phone)
        print(f"Found {len(contact_list)} contacts from file.")
    else:
        print("No existing contact file found. Starting fresh.")


def validate_name(name):
    if not name.isalpha():
        print("Error: The contact's name must contain only letters. Please try again.")
        return False
    return True

def validate_phone(phone):
    if not phone.isdigit():
        print("Error: The phone number must be digit. Please try again.")
        return False
    return True



load_contacts()  # Load existing contacts at the start of the program

while True:
    print("\nChoose an operation:")
    print("0: Exit")
    print("1: Add Contact")
    print("2: Remove Contact")
    print("3: Search Contacts")
    print("4: View Contacts")
    option = input("Enter your operation: ")

    if option == '0':
        print("Saving all contacts to file...")
        saving.save_all_contacts(contact_list)
        print("Contacts saved successfully. Exiting program.")
        break

    elif option == '1':
        print("Enter the details for the new contact:")
        # Validate name
        name = input("Name: ")
        if not validate_name(name):
            continue
        # Validate phone
        phone = input("Phone (unique & digit): ")
        if not validate_phone(phone):
            continue


        phone = int(phone)
        if phone in nums_collection:
            print("Error: Duplicate phone number detected. Please try again.")
            continue
        email = input("Email: ")
        address = input("Address: ")
        adding.add_contact(name, phone, email, address,contact_list,nums_collection)
        print("Contact added successfully.")

    elif option == '2':
        phone_to_remove = input("Enter the phone number of the contact to remove: ")
        if not phone_to_remove.isdigit():
            print("Invalid input. Please enter a valid numeric phone number.")
        else:
            removing.remove_contact(phone_to_remove, contact_list,nums_collection)

    elif option == '3':
        search_term = input("Enter a name, phone, email, or address to search: ")
        searching.search_contact(search_term,contact_list)

    elif option == '4':
        print("\nStored Contacts:")
        for contact in contact_list:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
    else:
        print("Invalid option. Please try again.")


