contacts = {}
def add_contact():
    name = input("Enter name:")
    number = input("Enter number:")
    contacts[name] = number
    print("Contact added")

def view_contact():
    if not contacts:
        print ("No contacts")
    else:
        for name, number in contacts.items():
            print (f"{name} : {number}")

def search_contact():
    name = input("Enter name to find:")
    if name in contacts:
        print (f"Found : {contacts[name]}")
    else:
        print("Not Found")

def delete_contact():
    name = input ("Enter name to delete:")
    if name in contacts:
        del contacts[name]
        print ("Contact Deleted")
    else:
        print("Not Found")

while True:
    print("\n --- Contacts Book --- ")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exiting the Contact Book")

    choice = input("Enter Choice:")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting....")
        break
    else:
        print("Invalid choice")