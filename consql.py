from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Contact(BaseModel):
    name: str
    number: int

def create_database():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS contacts  (
              name TEXT,
              number INTEGER
    )""")
    conn.commit()
    conn.close()

def add_contact(contact: Contact):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''INSERT INTO contacts (name, number) VALUES (?, ?)''', (contact.name, contact.number))
    conn.commit()
    conn.close()

def get_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM contacts''')
    contacts = c.fetchall()
    conn.close()
    return contacts

def delete_contact(name: str):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''DELETE FROM contacts WHERE name = ?''', (name,))
    conn.commit()
    deleted = c.rowcount > 0
    conn.close()
    return deleted

@app.post("/add_contact/")
async def add_contact_route(contact: Contact):
    add_contact(contact)
    return {"message": "Contact added"}

@app.get("/get_contacts/")
async def get_contacts_route():
    contacts = get_contacts()
    if not contacts:
        raise HTTPException(status_code=404, detail="No contacts found")
    return contacts

@app.delete("/delete_contact/{name}")
async def delete_contact_route(name: str):
    deleted = delete_contact(name)
    if deleted:
        return {"message": f"Contact '{name}' deleted"}
    else:
        raise HTTPException(status_code=404, detail="Contact not found")

if __name__ == "__main__":
    create_database()
