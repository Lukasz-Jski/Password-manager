from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="#F5EFE6")


canvas = Canvas(width=260, height=260, bg="#F5EFE6", highlightthickness=0)
# 224 - o jeden więcej żeby pracować łatwiej, na liczbach parzystych
padlock_img = PhotoImage(file="padlock.png")
canvas.create_image(130, 130, image=padlock_img) #połówki żeby obraz był wyśrodkowany
canvas.grid(column=1, row=0, pady=20)

website = Label(text="Website:", font=("Verdana", 10), bg="#F5EFE6")
website.grid(column=0, row=1, pady=2)

enter_website = Entry(width=60)
enter_website.grid(column=1, row=1, columnspan=2, pady=2)

username = Label(text="Email / Username:", font=("Verdana", 10), bg="#F5EFE6")
username.grid(column=0, row=2)

enter_user = Entry(width=60)
enter_user.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:", font=("Verdana", 10), bg="#F5EFE6")
password.grid(column=0, row=3)

new_password = Entry(width=42)
new_password.grid(column=1, row=3)

generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=50)
add_btn.grid(column=1, row=4, columnspan=2, pady=5)

















window.mainloop()






























