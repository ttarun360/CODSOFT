from tkinter import *
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if name and phone:
        contact_list.insert(END, f"{name} - {phone}")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please enter both name and phone number.")

def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        contact_list.delete(selected_index)
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

def clear_contacts():
    contact_list.delete(0, END)

def get_selected_contact(event):
    try:
        selected_index = contact_list.curselection()[0]
        selected_contact = contact_list.get(selected_index)
        name, phone = selected_contact.split(" - ")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        name_entry.insert(END, name)
        phone_entry.insert(END, phone)
    except IndexError:
        pass

def search_contact():
    query = search_entry.get().lower()
    for i in range(contact_list.size()):
        contact = contact_list.get(i).lower()
        if query in contact:
            contact_list.selection_clear(0, END)
            contact_list.selection_set(i)
            contact_list.activate(i)
            return

def update_contact():
    try:
        selected_index = contact_list.curselection()[0]
        name = name_entry.get()
        phone = phone_entry.get()

        if name and phone:
            contact_list.delete(selected_index)
            contact_list.insert(selected_index, f"{name} - {phone}")
            name_entry.delete(0, END)
            phone_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Please enter both name and phone number.")
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

root = Tk()
root.title("Phone Contacts")
root.geometry("400x600")
root.config(bg="#3498DB")

header_label = Label(root, text="Contacts", font=("Helvetica", 20), bg="#2980B9", fg="white", padx=10, pady=5)
header_label.pack(fill=X)

name_label = Label(root, text="Name:", font=("Helvetica", 14), bg="#3498DB", fg="white")
name_label.pack(pady=5)
name_entry = Entry(root, font=("Helvetica", 14))
name_entry.pack(pady=5)

phone_label = Label(root, text="Phone:", font=("Helvetica", 14), bg="#3498DB", fg="white")
phone_label.pack(pady=5)
phone_entry = Entry(root, font=("Helvetica", 14))
phone_entry.pack(pady=5)

add_button = Button(root, text="Add Contact", font=("Helvetica", 14), command=add_contact, bg="#2ECC71", fg="white")
add_button.pack(pady=10)

delete_button = Button(root, text="Delete Contact", font=("Helvetica", 14), command=delete_contact, bg="#E74C3C", fg="white")
delete_button.pack(pady=5)

clear_button = Button(root, text="Clear Contacts", font=("Helvetica", 14), command=clear_contacts, bg="#F39C12", fg="white")
clear_button.pack(pady=5)

update_button = Button(root, text="Update Contact", font=("Helvetica", 14), command=update_contact, bg="#3498DB", fg="white")
update_button.pack(pady=5)

search_entry = Entry(root, font=("Helvetica", 14))
search_entry.pack(pady=5)

search_button = Button(root, text="Search Contact", font=("Helvetica", 14), command=search_contact, bg="#3498DB", fg="white")
search_button.pack(pady=5)

contact_list = Listbox(root, font=("Helvetica", 14), bg="#1F618D", fg="white", selectbackground="#3498DB", height=10)
contact_list.pack(pady=10, fill=BOTH, expand=True)

contact_list.bind('<<ListboxSelect>>', get_selected_contact)

root.mainloop()
