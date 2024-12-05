import saving

# Function to remove a contact by phone number
def remove_contact(phone,contact_list,nums_collection):
    phone = int(phone)
    flag = False
    for contact in contact_list:
        if contact.phone==phone:
            contact_list.remove(contact)
            flag = True
            break

    if flag==True:
        nums_collection.remove(phone)  # Remove the phone number from the set
        saving.save_all_contacts(contact_list)  # Save the updated list to the file
        print("Contact removed successfully.")
    else:
        print("No contact found with the given phone number.")



