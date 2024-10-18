from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    import random as r

    letters = ['a','b','c','d', 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']

    numbers = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '0']

    symbols = ['!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' , ')' , '-' , '+' , '.']

    ln_letters = r.randint(7,12)
    ln_numbers = r.randint(4,9)
    ln_symbols = r.randint(4,6)

    password_list = []

    for char in range(1,ln_letters +1 ):
        random_num = r.randint(0,len(letters)-1)
        password_list.append(letters[random_num])

    for sym in range(1,ln_symbols +1 ):
        random_num = r.choice(symbols)
        password_list.append(random_num)

    for num in range(1,ln_numbers +1 ):
        random_num = r.choice(numbers)
        password_list.append(random_num)


    # print(password_list)

    # shuffle(list_name) is a reorder the element
    r.shuffle(password_list)
    # print(password_list)
    password =""

    for passw in range(0, 15):
        password += password_list[passw]
    
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    new_data = {
        website_entry.get().title():{
            "Email":username_entry.get(),
            "Password":password_entry.get()
        }
    }

    if website_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "" :
        is_ok = messagebox.showwarning(title="Oops", message="please don't leave any fields empty!" )
    else:
        is_ok = messagebox.askokcancel(title="Conform", message=f"Enter your details\n Email: {username_entry.get()}  password: {password_entry.get()}\n please ok to save ")

        if is_ok:
            try:
                with open("data.json",mode="r") as file:
                    # reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json",mode="w") as file:
                    json.dump(new_data,file,indent=4)
            else:
                # updata old data with new data
                data.update(new_data)
                
                with open("data.json",mode="w") as file:
                    #insert new data in json file
                    json.dump(data,file,indent=4)
    
            website_entry.delete(0,END)
            # username_entry.delete(0,END)
            password_entry.delete(0,END)


# -------------------------find password------------------------------# 

def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file  found")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website , message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="error", message=f"No details for {website} exists")
            



    


# ---------------------------- UI SETUP ------------------------------- #


window  = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas =  Canvas(width=200,height=200)
image_name = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= image_name )
canvas.grid(row=0,column=1,columnspan=2)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


# entry
website_entry = Entry(width=20)
website_entry.grid(row=1,column=1)
website_entry.focus()
username_entry = Entry(width=40)
username_entry.grid(row=2,column=1,columnspan=2)
username_entry.insert(0, "prit@gmail.com")
password_entry =Entry(width=20)
password_entry.grid(row=3,column=1)


# button
genrate_button = Button(text="Genarate Password", command=password)
# genrate_button.config(highlightthickness=0)
genrate_button.grid(row=3,column=2)
add_button  =Button(text="Add",width=34,command=save_data)
# add_button.config(highlightthickness=0)
add_button.grid(row=4,column=1, columnspan=2)
search_button = Button(text="Search",width=15,command=find_password)
search_button.grid(row=1,column=2)




window.mainloop()
