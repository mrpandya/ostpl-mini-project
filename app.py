from whatsapp_sender.sender import MessageSender as ms
import tkinter as tk
from tkinter import messagebox

def filter_contact_names(contacts:str):
    '''
    :params contacts: comma separated string of all the contacts
    :return list of contact names
    '''
    contact_names = list(contacts.split(','))
    contact_names = [i.strip(' ') for i in contact_names]
    return contact_names

def check_string(string:str):
    '''
    :param message: string to be checked if empty or not
    :return True if string is not empty
    '''
    if string.strip(" ").__len__() >1:
        return True
    return False

def check_data(contacts:str,message:str):

    for label in window.grid_slaves():
      if int(label.grid_info()["column"]) == 2:
           label.grid_forget()

    if not check_string(contacts):
        error_message = tk.Message(window,text="Error : Please enter comma separated Contacts, minimum number of contacts = 1")
        error_message.config(bg='red')
        error_message.grid(row=0,column=2)
        return False
    if not check_string(message):
        error_message=tk.Message(window,text="Error : The message should have more than 1 character and it cannot be space")
        error_message.config(bg='red')
        error_message.grid(row=1,column=2)
        return False
    return True

def send_message(contacts:str,message:str):
    if not check_data(contacts,message):
        return False
    object = ms(browser="firefox")
    contacts = filter_contact_names(contacts)
    if object.send_messages(contacts,message):
        messagebox.showinfo("Success",  "Your Messages have been sent to "+' '.join(contacts))
        window.destroy()


window = tk.Tk()
window.title('Whatsapp Sender')
tk.Label(window, text='Contacts').grid(row=0)
tk.Label(window, text='Message').grid(row=1)
e1 = tk.Entry(window)
e2 = tk.Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
button = tk.Button(window, text='Send', width=25, command=lambda:send_message(e1.get(),e2.get()))
button.grid(row=2, column=1)
# button = tk.Button(window, text='Send', width=25, command=window.destroy)
window.mainloop()

# Hello Bitch, I am just testing my python project feel free to ignore this message but dare you ignore me