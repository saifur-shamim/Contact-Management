
# Function to search for contacts
def search_contact(search_term,contact_list):
    results = [contact for contact in contact_list if
               search_term.lower() in contact.name.lower() or
               search_term.lower() in contact.email.lower() or
               search_term.lower() in contact.address.lower() or
               search_term == str(contact.phone)]

    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
    else:
        print("No contacts found matching the search term.")