def add_contacts(name, number):
    contact = {name: {'phone': number}}
    with open("file2.txt", "a") as file:
         file.write(f"{name}: {{'phone': '{number}'}}\n")
    print("Contact added")


def search_contacts(name):
    with open("file2.txt", "r") as file:
        for line in file:
            try:
                contact = eval(line)
            except SyntaxError:
                continue
            if name in contact:
                print(f"Contact found: {name}: {contact[name]}")
                return
        print("contact not found")

def delete_contacts(name):
    contact_to_keep = []
    with open("file2.txt", "r") as file:
        for line in file:
            contact = eval(line)
            if name not in contact:
                contact_to_keep.append(contact)
    with open("file2.txt", "w") as file:
        for contact in contact_to_keep:
            file.write(str(contact) + "\n")
        print("contact deleted")

def show_all_contacts():
    with open("file2.txt", "r") as file:
        contacts = file.readlines()
        if not contacts:
            print("No contacts found")
            return
        print("Contacts: ")
        for contact in contacts:
            contact_dict = eval(contact.strip())
            for name, info in contact_dict.items():
                phone = info['phone']
                print(f"{name}: {phone}")

def main():

    while True:
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Show all contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contacts(name, number)

        if choice == "2":
            name = input("Enter the contact name to search: ")
            search_contacts(name)

        elif choice == "3":
            name = input("Enter contact name to delete: ")
            delete_contacts(name)

        elif choice == "4":
            show_all_contacts()

            
        elif choice == "5":
            print("Bye!")
            break
        

if __name__ == "__main__":
    main()

            