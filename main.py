from tkinter import * # import all classes
from tkinter import messagebox # is a module not a class
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    numbers_list = [random.choice(symbols) for _  in range(random.randint(2, 4))]
    symbols_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list # Joining all the above list into a big list
    random.shuffle(password_list)
    password = "".join(password_list) #joins the list 
    password_entry.insert(0, password) # Populating the password_entry with password
    
    # copy the password to the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    # Validation
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title= website, message= f"These are the details entered: \nEmail: {email} \nPassword: {password}"
                            f"\nIs it ok to save?")
        
        if is_ok: # returns boolean value(true or false)
            with open("./password-manager-start/Data.txt", "a") as myfile:
                myfile.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

canvas = Canvas(width=200, height= 200)
logo_img = PhotoImage(file= "./password-manager-start/logo.png")
img = canvas.create_image(100, 100, image= logo_img)
canvas.grid(column= 1, row= 0)

# Labels
website_label = Label(text= "Website:")
website_label.grid(column= 0, row= 1)
email_label = Label(text= "Email/Username:") 
email_label.grid(column= 0, row= 2)
password_label = Label(text= "Password:")
password_label.grid(column= 0, row= 3)

# Entries
website_entry = Entry(width= 50)
website_entry.grid(column= 1, columnspan= 2, row= 1)
website_entry.focus() 
email_entry = Entry(width= 50)
email_entry.grid(column= 1, columnspan= 2, row= 2)
email_entry.insert(0, "qwerty@gmail.com")
password_entry = Entry(width= 32)
password_entry.grid(column=1, row= 3)


# Button 
generate_button = Button(text= "Generate Password", command= generate_password)
generate_button.grid(column= 2, row= 3)
add_button = Button(text= "Add", width= 42, command= save)
add_button.grid(column= 1, columnspan= 2, row= 4)

window.mainloop()
