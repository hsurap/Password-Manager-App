import  tkinter
import random
import pyperclip
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list+=[random.choice(letters) for i in range(0,nr_letters)]
    password_list+=[random.choice(symbols) for i in range(0,nr_symbols)]
    password_list+=[random.choice(numbers) for i in range(0,nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}"
    pass_inp.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=web_inp.get()
    email=email_inp.get()
    password=pass_inp.get()
    check=True
    if len(website)==0 or len(email)==0 or len(password)==0:
        check =False
    if check==False:
        tkinter.messagebox.showwarning(title="Oops",message="Please don't leave any field empty!")
    is_ok=False
    if check==True:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \n EmailL: {email} \n Password: {password}\n Is is ok to save ?")
    if is_ok :
        with open("data.txt","a") as file:
            file.write(f"{website} | {email} | {password}\n")
        clear_data()


def clear_data():
    web_inp.delete(0,tkinter.END)
    email_inp.delete(0,tkinter.END)
    pass_inp.delete(0,tkinter.END)
    email_inp.insert(0, "parush@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #


window=tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = tkinter.Canvas( width = 200, height = 200)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=img)
canvas.grid(row=0,column=1)

#Label
website_label=tkinter.Label(text="Website: ")
website_label.grid(row=1,column=0)

email_label=tkinter.Label(text="Email/Username: ")
email_label.grid(row=2,column=0)

password_label=tkinter.Label(text="Password: ")
password_label.grid(row=3,column=0)

#Entry
web_inp=tkinter.Entry(width=35)
web_inp.grid(row=1,column=1,columnspan=2)
web_inp.focus()

email_inp=tkinter.Entry(width=35)
email_inp.grid(row=2,column=1,columnspan=2)
email_inp.insert(0,"parush@gmail.com")

pass_inp=tkinter.Entry(width=17)
pass_inp.grid(row=3,column=1)

#Button
gen_pass=tkinter.Button(text="Generate Password",command=generatePassword)
gen_pass.grid(row=3,column=2)

add=tkinter.Button(text="Add",width=36,command=save)
add.grid(row=4,column=1,columnspan=2)



window.mainloop()