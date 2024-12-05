
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

# Function to add a new contact
def add_contact(name, phone, email, address,contact_list, nums_collection):
    # Create a Contact object and append it to the list
    new_contact = Contact(name, phone, email, address)
    nums_collection.add(phone)
    contact_list.append(new_contact)