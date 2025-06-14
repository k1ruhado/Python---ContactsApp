import tkinter as tk
from tkinter import messagebox
import os

def load_contacts():
    contacts = []
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r", encoding="utf-8") as file:
            for line in file:
                contacts.append(line.strip().split(","))
    return contacts

def save_contacts(contacts):
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for contact in contacts:
            file.write(",".join(contact) + "\n")

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    if name and phone and email:
        contacts.append([name, phone, email])
        save_contacts(contacts)
        messagebox.showinfo("Успіх", "Контакт додано!")
        clear_entries()
        choice = messagebox.askyesno("Вибір", "Показати всю книжку? (Ні = Пошук)")
        if choice:
            show_all_contacts()
        else:
            entry_search.focus_set()
    else:
        messagebox.showwarning("Помилка", "Заповни всі поля!")

def show_all_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact[0]} - {contact[1]} - {contact[2]}")

def search_contacts():
    search_term = entry_search.get().lower()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if search_term in contact[0].lower() or search_term in contact[1] or search_term in contact[2].lower():
            contact_list.insert(tk.END, f"{contact[0]} - {contact[1]} - {contact[2]}")

def edit_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        if name and phone and email:
            contacts[index] = [name, phone, email]
            save_contacts(contacts)
            messagebox.showinfo("Успіх", "Контакт оновлено!")
            show_all_contacts()
            clear_entries()
        else:
            messagebox.showwarning("Помилка", "Заповни всі поля!")
    else:
        messagebox.showwarning("Помилка", "Вибери контакт!")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        del contacts[index]
        save_contacts(contacts)
        messagebox.showinfo("Успіх", "Контакт видалено!")
        show_all_contacts()
    else:
        messagebox.showwarning("Помилка", "Вибери контакт!")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

root = tk.Tk()
root.title("Контакти")

label_name = tk.Label(root, text="ПІБ:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_phone = tk.Label(root, text="Телефон:")
label_phone.grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

label_email = tk.Label(root, text="E-mail:")
label_email.grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

button_add = tk.Button(root, text="Додати контакт", command=add_contact)
button_add.grid(row=3, column=0, columnspan=2)

button_show_all = tk.Button(root, text="Показати всі контакти", command=show_all_contacts)
button_show_all.grid(row=4, column=0, columnspan=2)

label_search = tk.Label(root, text="Пошук:")
label_search.grid(row=5, column=0)
entry_search = tk.Entry(root)
entry_search.grid(row=5, column=1)
button_search = tk.Button(root, text="Пошук", command=search_contacts)
button_search.grid(row=6, column=0, columnspan=2)

button_edit = tk.Button(root, text="Редагувати контакт", command=edit_contact)
button_edit.grid(row=7, column=0, columnspan=2)

button_delete = tk.Button(root, text="Видалити контакт", command=delete_contact)
button_delete.grid(row=8, column=0, columnspan=2)

contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=9, column=0, columnspan=2)

contacts = load_contacts()
show_all_contacts()

label_footer = tk.Label(root, text="Made by k1ruha with ❤️", font=("Arial", 10, "bold"))
label_footer.grid(row=10, column=0, columnspan=2, sticky="s")

root.mainloop()