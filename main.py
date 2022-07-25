import tkinter
from tkinter import messagebox
from password_generator import password_gen
import pyperclip
import json


# ---------------------------- SEARCHING ------------------------------- #

def search():
    web_name = entry_website.get()
    if web_name == "":
        messagebox.showerror(title="Error", message="You must input website name!")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                web = data[web_name]
                em_usr = web['email/username']
                password = web['password']
                if len(em_usr) == 0 :
                    messagebox.showinfo(title="Search Result", message="Sorry! Email not found")
                elif len(password) == 0:
                    messagebox.showinfo(title="Search Result", message="Sorry! password not found")
                else: 
                    messagebox.showinfo(title="Search Result", message=f"Website: {web_name} \nUsername/Email: {em_usr} \nPassword: {password} ")
        except:
            messagebox.showinfo(title="Search Result", message="Sorry! There is no data available or 'data.json' file not found")
        else:
            pyperclip.copy(password)
        
        
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    entry_password.delete(0, 'end')
    password = password_gen()
    pyperclip.copy(password)
    entry_password.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    web_name = entry_website.get()
    em_usrnm = entry_em_usrnm.get()
    password = entry_password.get()
    
    new_data = {
        web_name : {
            "email/username" : em_usrnm,
            "password" : password
        }
    }
    
    if web_name == "":
        messagebox.showerror(title="Error", message="You must input website name!")
    elif em_usrnm == "":
        messagebox.showerror(title="Error", message="You must input Email/Username name!")
    elif password == "":
        messagebox.showerror(title="Error", message="You must input Password!")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Website: {web_name} \nEmail/Username: {em_usrnm} \nPassword: {password}")

        if is_ok:
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
                    data.update(new_data)
            except:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
            finally:
                entry_website.delete(0, "end")
                entry_password.delete(0, 'end')

        
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
# window.minsize(width=560, height=560)
window.title("Password Manager")
window.geometry("670x526")

canvas = tkinter.Canvas(width=300, height=300)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_img)
canvas.place(x=192, y=36)

label_website = tkinter.Label(text="Website : ", font=("Arial", 12))
label_website.place(x=120, y=370)

entry_website = tkinter.Entry(width=50)
entry_website.focus()
entry_website.place(x=225, y=372)

label_em_usrnm = tkinter.Label(text="Email/Username: ", font=("Arial", 12))
label_em_usrnm.place(x=85, y=400)

entry_em_usrnm = tkinter.Entry(width=50)
entry_em_usrnm.insert(1, "ashik@gmail.com")
entry_em_usrnm.place(x=225, y=402)

label_password = tkinter.Label(text="Password: ", font=("Arial", 12))
label_password.place(x=115, y=430)

entry_password = tkinter.Entry(width=50)
entry_password.place(x=225, y=432)

button_gen_pass = tkinter.Button(text="Generate Password", command=pass_gen)
button_gen_pass.place(x=418, y=452)

button_search = tkinter.Button(text="Search", command=search)
button_search.place(x=225, y=452)

button_add = tkinter.Button(text="Add", width=42, command=save)
button_add.place(x=225, y=480)

window.mainloop()