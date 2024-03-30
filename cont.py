import json
import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        
        self.contact_book = ContactBook()
        
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(master, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, sticky="e")
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="e")
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.display_button = tk.Button(master, text="Display Contacts", command=self.display_contacts)
        self.display_button.grid(row=4, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone_number and email:
            contact = Contact(name, phone_number, email)
            self.contact_book.add_contact(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def display_contacts(self):
        contacts = self.contact_book.get_contacts()
        if contacts:
            contact_info = "\n".join([f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}" for contact in contacts])
            messagebox.showinfo("Contacts", contact_info)
        else:
            messagebox.showinfo("Contacts", "No contacts found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_contacts(self):
        return self.contacts

def main():
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
