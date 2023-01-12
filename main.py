from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="#F5EFE6")


canvas = Canvas(width=480, height=520, bg="#F5EFE6", highlightthickness=0)
# 224 - o jeden więcej żeby pracować łatwiej, na liczbach parzystych
padlock_img = PhotoImage(file="padlock.png")
canvas.create_image(240, 260, image=padlock_img) #połówki żeby obraz był wyśrodkowany
canvas.grid(column=1, row=1)








# 7DE5ED




window.mainloop()






























