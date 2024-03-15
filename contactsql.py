import sqlite3
def create_database():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS contacts  (
              name TEXT,
              number TEXT
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
    if contacts:
        for contact in contacts:
            print(f"Name: {contact[0]}, Number: {contact[1]}")
    else:
        print("no contacts found")
        conn.close()

def delete_contacts(name):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''DELETE FROM contacts WHERE name = ?''', (name,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    while True:
        print("\n1. Add contact\n2. show contacts\n3. delete contact\n4. exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            number = input("enter number: ")
            add_contacts(name, number)
            print("contact added")
        
        elif choice == '2':
            show_contacts()

        elif choice == '3':
            name = input("enter the name of the contact to delete: ")
            delete_contacts(name)
            print("contact deleted")

        elif choice == '4':
            print("BYE!")
            break

        else:
            print("invalid choice, enter again")


        
              