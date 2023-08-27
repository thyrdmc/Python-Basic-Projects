import random
from tkinter import *
from tkinter import messagebox
import pandas
# Copies Password from Application
import pyperclip
import json


def generate_password():
    """ Generates Password for Security """

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # List Comprehension Structure

    pw_letters = [random.choices(letters) for i in range(random.randint(8, 10))]
    pw_symbols = [random.choices(symbols) for i in range(random.randint(2, 4))]
    pw_numbers = [random.choices(numbers) for i in range(random.randint(2, 4))]

    pw_list = pw_letters + pw_symbols + pw_numbers

    # Shuffling to List

    random.shuffle(pw_list)

    # List to String Conversion

    password = ''

    for j in pw_list:
        password += j[0]

    txt_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #

# Generates User Screen
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

# Generates Canvas for UI Materials
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

lblWebsite = Label(text='Website/Social Media :')
lblWebsite.grid(row=1, column=0)

txt_website = Entry(width=38)
txt_website.grid(row=1, column=1, columnspan=2)
txt_website.focus()

lblUsername = Label(text='Email/Username :')
lblUsername.grid(row=2, column=0)

txt_username = Entry(width=38)
txt_username.grid(row=2, column=1, columnspan=2)

# Autofilled Mail Textbox
txt_username.insert(0, 'test@gmail.com')

lblPassword = Label(text='Password :')
lblPassword.grid(row=3, column=0)

txt_password = Entry(width=21)
txt_password.grid(row=3, column=1)

btn_generate = Button(text="Generate Password", command=generate_password, width=13)
btn_generate.grid(row=3, column=2)


def save_text():
    """Stores User Information in info.txt File"""
    website = txt_website.get()
    username = txt_username.get()
    password = txt_password.get()
    user_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if txt_username.get() == '' or txt_username.get() == '' or txt_password.get() == '':
        messagebox.showinfo(title="Information", message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open("data.json", 'r') as f:
                # Reading Old Data
                data = json.load(f)

        except:
            with open("data.json", 'w') as f:
                json.dump(user_data, f, indent=4)

        else:
            # Updating Old Data
            data.update(user_data)

            with open("data.json", 'w') as f:
                # Saving Updated Data
                json.dump(data, f, indent=4)

        finally:
            txt_password.delete(0, END)
            txt_website.delete(0, END)


btn_add = Button(text="Add", command=save_text, width=36, fg="black", highlightthickness=0)
btn_add.grid(row=4, column=1, columnspan=2)

screen.mainloop()
