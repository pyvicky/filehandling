def add_contacts(name, number):
    contact = {name: {'phone': number}}
    with open("file3.txt", "a") as file:
         file.write(f"{name}: {{'phone': '{number}'}}\n")
    print("Contact added")

def show_contacts():
    try:
        with open("file3.txt", "r") as file:
            contacts = file.readlines()
            if contacts:
                print("Contacts:")
                for contact in contacts:
                    print(contact.strip())
            else:
                print("No contacts found.")
    except FileNotFoundError:
        print("No contacts found.")

def delete_contact(name):
    try:
        with open("file3.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No contacts found.")
        return

    with open("file3.txt", "w") as file:
        deleted = False
        for line in lines:
            if not line.startswith(name + ":"):
                file.write(line)
            else:
                deleted = True
        if deleted:
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")


def main():
    while True:
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            add_contacts(name, number)
        
        elif choice == "2":
            show_contacts()
        
        elif choice == "3":
            name = input("Enter name to delete: ")
            delete_contact(name)
        
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()