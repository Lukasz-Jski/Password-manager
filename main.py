from tkinter import *
from tkinter import messagebox
import random
import json

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="#F5EFE6")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [random.choice(letters) for letter in range(random.randint(6, 10))]
    random_numbers = [random.choice(numbers) for number in range(random.randint(2, 6))]
    random_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 6))]

    characters_list = random_letters + random_numbers + random_symbols

    random.shuffle(characters_list)
    random_password = "".join(characters_list)
    new_password.delete(0, END)
    new_password.insert(0, random_password)


def save_data():
    stored_data = {
        enter_website.get(): {
            "email": enter_user.get(),
            "password": new_password.get()
        }
    }
    if len(enter_website.get()) == 0 or len(enter_user.get()) == 0 or len(new_password.get()) == 0:
        messagebox.showwarning(title="Error", message="Please fill all the empty fields.")
    else:
        yes = messagebox.askyesno(title="Saving", message=f"Are you sure you want to save these details? "
                                          f"\n{enter_website.get()}\n{enter_user.get()}\n{new_password.get()}")
        if yes:
            try:
                with open("data.json", "r") as data:
                    data_file = json.load(data)
            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(stored_data, data, indent=4)
            else:
                data_file.update(stored_data)
                with open("data.json", "w") as data:
                    json.dump(data_file, data, indent=4)
            finally:
                enter_website.delete(0, END)
                enter_user.delete(0, END)
                new_password.delete(0, END)


canvas = Canvas(width=260, height=260, bg="#F5EFE6", highlightthickness=0)
padlock_img = PhotoImage(file="padlock.png")
canvas.create_image(130, 130, image=padlock_img)
canvas.grid(column=1, row=0, pady=20)

website = Label(text="Website:", font=("Verdana", 10), bg="#F5EFE6")
website.grid(column=0, row=1, pady=2)

enter_website = Entry(width=60)
enter_website.focus()
enter_website.grid(column=1, row=1, columnspan=2, pady=2)

username = Label(text="Email / Username:", font=("Verdana", 10), bg="#F5EFE6")
username.grid(column=0, row=2)

enter_user = Entry(width=60)
enter_user.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:", font=("Verdana", 10), bg="#F5EFE6")
password.grid(column=0, row=3)

new_password = Entry(width=42)
new_password.grid(column=1, row=3)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=50, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, pady=5)


window.mainloop()