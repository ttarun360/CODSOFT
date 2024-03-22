import string
import random
from tkinter import *
from tkinter import messagebox
import sqlite3


with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT NOT NULL, GeneratedPassword TEXT NOT NULL);")
cursor.execute("SELECT * FROM users")
db.commit()
db.close()


class GUI():
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()

        root.title('Password Generator')
        root.geometry('400x300')
        root.config(bg='#FF8000')
        root.resizable(False, False)

        self.label = Label(text="PASSWORD GENERATOR", anchor=N, fg='darkblue', bg='#FF8000', font='arial 16 bold underline')
        self.label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        self.user = Label(text="Enter User Name:", font='times 12 bold', bg='#FF8000', fg='darkblue')
        self.user.grid(row=1, column=0, padx=10, pady=5)

        self.textfield = Entry(textvariable=self.username, font='times 12', bd=6, relief='ridge')
        self.textfield.grid(row=1, column=1, padx=10, pady=5)
        self.textfield.focus_set()

        self.length = Label(text="Enter Password Length:", font='times 12 bold', bg='#FF8000', fg='darkblue')
        self.length.grid(row=2, column=0, padx=10, pady=5)

        self.length_textfield = Entry(textvariable=self.passwordlen, font='times 12', bd=6, relief='ridge')
        self.length_textfield.grid(row=2, column=1, padx=10, pady=5)

        self.generated_password = Label(text="Generated Password:", font='times 12 bold', bg='#FF8000', fg='darkblue')
        self.generated_password.grid(row=3, column=0, padx=10, pady=5)

        self.generated_password_textfield = Entry(textvariable=self.generatedpassword, font='times 12', bd=6, relief='ridge', fg='#DC143C')
        self.generated_password_textfield.grid(row=3, column=1, padx=10, pady=5)

        self.generate = Button(text="Generate Password", bd=3, relief='solid', padx=5, pady=5, font='Verdana 12 bold', fg='#68228B', bg='#BCEE68', command=self.generate_pass)
        self.generate.grid(row=4, column=0, columnspan=2, pady=10)

        self.accept = Button(text="Accept", bd=3, relief='solid', padx=5, pady=5, font='Helvetica 12 bold italic', fg='#458B00', bg='#FFFAF0', command=self.accept_fields)
        self.accept.grid(row=5, column=0, columnspan=2, pady=5)

        self.reset = Button(text="Reset", bd=3, relief='solid', padx=5, pady=5, font='Helvetica 12 bold italic', fg='#458B00', bg='#FFFAF0', command=self.reset_fields)
        self.reset.grid(row=6, column=0, columnspan=2, pady=5)

    def generate_pass(self):
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        chars = "@#%&()\"?!"
        numbers = "1234567890"
        upper = list(upper)
        lower = list(lower)
        chars = list(chars)
        numbers = list(numbers)
        name = self.textfield.get()
        leng = self.length_textfield.get()

        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()

        if name == "":
            messagebox.showerror("Error", "Name cannot be empty")
            return

        if name.isalpha() == False:
            messagebox.showerror("Error", "Name must be a string")
            self.textfield.delete(0, 25)
            return

        length = int(leng)

        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long")
            self.textfield.configure(text="")
            return

        self.generated_password_textfield.delete(0, length)

        u = random.randint(1, length-3)
        l = random.randint(1, length-2-u)
        c = random.randint(1, length-1-u-l)
        n = length-u-l-c

        password = random.sample(upper, u) + random.sample(lower, l) + random.sample(chars, c) + random.sample(numbers, n)
        random.shuffle(password)
        gen_passwd = "".join(password)
        n_generatedpassword = self.generated_password_textfield.insert(0, gen_passwd)

    def accept_fields(self):
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            find_user = ("SELECT * FROM users WHERE Username = ?")
            cursor.execute(find_user, [(self.username.get())])

            if cursor.fetchall():
                messagebox.showerror("This username already exists!", "Please use another username")
            else:
                insert = str("INSERT INTO users(Username, GeneratedPassword) VALUES(\'%s\', \'%s\');" % (self.username.get(), self.generatedpassword.get()))
                cursor.execute(insert)
                db.commit()
                messagebox.showinfo("Success!", "Password generated successfully")

    def reset_fields(self):
        self.textfield.delete(0, 25)
        self.length_textfield.delete(0, 25)
        self.generated_password_textfield.delete(0, 25)


if __name__ == '__main__':
    root = Tk()
    pass_gen = GUI(root)
    root.mainloop()
