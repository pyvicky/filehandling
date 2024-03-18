import sqlite3
def create_database():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS contacts  (
              name TEXT,
              number INTEGER
    )""")
    conn.commit()
    conn.close()

def add_contacts(name, number):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''INSERT INTO contacts (name, number) VALUES (?, ?)''', (name, number))
    conn.commit()
    conn.close()

def show_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM contacts''')
    contacts = c.fetchall()
    for contact in contacts:
        print(f"Name: {contact[0]}, Number: {contact[1]}")
    if not contacts:
        print("No contacts found")
    conn.close()

def delete_contacts(name):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''DELETE FROM contacts WHERE name = ?''', (name,))
    conn.commit()
    if c.rowcount > 0:
        print("Contact deleted")
    else:
        print("Name not found, enter a valid name")
    conn.close()

if __name__ == "__main__":
    create_database()
    while True:
        print("\n1. Add contact\n2. show contacts\n3. delete contact\n4. exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = str(input("Enter name: "))
            try:
                number = int(input("Enter number: "))
                add_contacts(name, number)
                print("Contact added")
            except:
                print("Please enter a valid number!")
        
        elif choice == '2':
            show_contacts()

        elif choice == '3':
            name = input("enter the name of the contact to delete: ")
            delete_contacts(name)
            
        elif choice == '4':
            print("BYE!")
            break

        else:
            print("invalid choice, enter again")


        
              