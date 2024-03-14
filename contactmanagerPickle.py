import pickle

def add_contact(name, phone, contacts):
    contacts[name] = phone
    save_contacts(contacts)
    print("contact added")

def show_contacts(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("no contacts found.")

def delete_contact(name, contacts):
    if  name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contacts '{name}' deleted.")
    else:
        print(f"Contacts '{name}' not found.")

def save_contacts(contacts):
    with open("file4.pickle", "wb") as f:
        pickle.dump(contacts, f)

def load_contacts():
    try:
        with open("file4.pickle", "rb") as f:
            contacts = pickle.load(f)
    except FileNotFoundError:
        contacts = {}
    return contacts

def main():
    contacts = load_contacts()

    while True:
        print("1. Add contact")
        print("2. Show contacts")
        print("3. Delete contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter number: ")
            add_contact(name, phone, contacts)
        
        elif choice == "2":
            show_contacts(contacts)

        elif choice == "3":
             name = input("Enter the name to delete: ")
             delete_contact(name, contacts)

        elif choice == "4":
            print("Bye!")
            break
        else:
            print("invalid option, try again.")

if __name__ == "__main__":
    main()
              
