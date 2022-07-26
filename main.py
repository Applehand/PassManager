from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def random_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(random.choice(letters)) for n in range(random.randint(8, 10))]
    [password_list.append(random.choice(symbols)) for n in range(random.randint(2, 4))]
    [password_list.append(random.choice(numbers)) for n in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_field.insert(0, password)
    pyperclip.copy(password)


# ----------------------------------- Password Generation ---------------------------------------------

def add_data():
    if len(website_field.get()) == 0 or len(password_field.get()) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_field.get(),
                                       message=f"These are the details entered: \nWebsite: {website_field.get()}\nEmail: {emailuser_field.get()}\nPassword: {password_field.get()}\nSave creds?")
        if is_ok:
            with open('pass_data.txt', "a") as file:
                file.write(f"{website_field.get()} | {emailuser_field.get()} | {password_field.get()}\n")
                website_field.delete(0, END)
                emailuser_field.delete(0, END)
                password_field.delete(0, END)

            website_field.delete(0, END)
            password_field.delete(0, END)
            emailuser_field.delete(0, END)


# ---------------------------------------- UI ----------------------------------------------------

# Window and Image

window = Tk()
window.title('Password Manager')
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)

logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

emailuser_label = Label(text="Email/Username")
emailuser_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Fields
website_field = Entry(width=35)
website_field.focus()
website_field.grid(row=1, column=1, columnspan=2)

emailuser_field = Entry(width=35)
emailuser_field.grid(row=2, column=1, columnspan=2)

password_field = Entry(width=21)
password_field.grid(row=3, column=1)

# Buttons

generate_pass = Button(text='New Password', command=random_pass)
generate_pass.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
