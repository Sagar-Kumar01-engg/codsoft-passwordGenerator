from tkinter import *
import random
from tkinter import messagebox
import string

def generate_password():
    try:
       length = int(len_pass.get())
       Uppercase = var_uppercase.get()
       Digits = var_digits.get()
       Symobols = var_symbol.get()
    except ValueError:
        if length <= 4:
           messagebox.showwarning("Weak Password", "Length should be greater than 4")
           return
    
    character = string.ascii_lowercase
    if Uppercase:
        character += string.ascii_uppercase
    if  Digits:
        character += string.digits
    if Symobols:
        character += string.punctuation
    
    if not character:
        messagebox.showwarning("weak password", "Pick at least on option")
        return
    
    password = ''.join(random.choice(character) for _ in range(length)) 
    display_password.delete(0,END)
    display_password.insert(0,password)

    

root = Tk()
root.geometry("655x355")

len_pass = Entry(root, font="lucida 10 bold")
len_pass.pack(pady= 10)
l=Label(root, text="Make the lenth of passwrod")
l.pack(pady=5)

var_uppercase = BooleanVar()
var_digits = BooleanVar()
var_symbol = BooleanVar()

Checkbutton(root, text="Select Uppercase", variable=var_uppercase).pack()
Checkbutton(root, text="Select Digits", variable=var_digits).pack()
Checkbutton(root, text="Select Symbol", variable=var_symbol).pack()

f= Frame(root).pack()
b1 = Button(f, text="generate", font="lucida 15 bold", command=generate_password).pack()

display_password = Entry(root, font="lucida 30 bold")
display_password.pack(pady=30)
root.mainloop()