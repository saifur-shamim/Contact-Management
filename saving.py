

# Function to save all contacts to the file
def save_all_contacts(contact_list):
    with open("list.csv", "w") as fp:
        for contact in contact_list:
            line = f"{contact.name}, {contact.phone}, {contact.email}, {contact.address}\n"
            fp.write(line)