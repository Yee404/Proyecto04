# LOGIN
# Sign in, Sign up

import customtkinter
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Modulos_Proyecto4 import *


registros = Read()


customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')

APP = tk.Tk()
APP.title('Login')
APP.geometry('1000x600+250+100')
APP.configure(bg="#FFFFFF")
APP.resizable(False, False)



def p_signin():
    def SignIn():
        UserCreated = str(user.get())
        PasswordCreated = str(password.get())
        Exist = False
        for i in range(1,len(registros)):
            if (registros[i][0] == UserCreated and registros[i][1] == PasswordCreated):
                Exist = True
                APP.destroy()
                DIAGNOSTIC()
        if Exist == False:
            messagebox.showinfo(title = "Error", message = "Incorrect username or password")
    
    frame = tk.Frame(master=APP,width=400, height=500)
    frame.place(x=310,y=50)
    
    signinbutton = tk.Button(master=frame, width=10,pady=7,border=0,text='Sing In',font=('Roboto',12,'bold'))
    signinbutton.place(x=20,y=20)
    linea = tk.Frame(frame, width=80, height=2, bg='black').place(x=40, y=52)
    signupbutton = tk.Button(master=frame, width=10,pady=7,border=0,text='Sing Up',font=('Roboto',12,'bold'), command = p_signup)
    signupbutton.place(x=150,y=20)
            
    user = customtkinter.CTkEntry(master=frame, placeholder_text='Username', width=250, height= 35, corner_radius=4)
    user.place(x=80,y=200)

    password = customtkinter.CTkEntry(master=frame, placeholder_text='🔒 Password', width=250, height= 35, corner_radius=4)
    password.place(x=80,y=260)

    login = tk.Button(frame,width=20,pady=7,text='Login', bg='#BD81EB', fg='white', border=0, command= SignIn).place(x=130, y=400)

def p_signup():
    def Verify():
        newuser = str(user1.get())
        olduser = False
        for i in range(1,len(registros)):
            if (registros[i][0] == newuser):
                messagebox.showinfo(title = "Error", message = "Username already taken")
                olduser = True
        if olduser == False:
            password1 = str(password.get())
            password2 = str(passwordc.get())
            if (password1 == password2):
                new_user = [newuser,password1]
                registros.append(new_user)
                NuevoUsuario(new_user)
                messagebox.showinfo(title = "", message = "Account Created!")
                p_signin()
            else:
                messagebox.showinfo(title = "Error", message = "Passwords do not match. Try Again.")
    
    frame = tk.Frame(master=APP,width=400, height=500)
    frame.place(x=310,y=50)
    
    signinbutton = tk.Button(master=frame, width=10,pady=7,border=0,text='Sing In',font=('Roboto',12,'bold'), command= p_signin)
    signinbutton.place(x=20,y=20)

    signupbutton = tk.Button(master=frame, width=10,pady=7,border=0,text='Sing Up',font=('Roboto',12,'bold'))
    signupbutton.place(x=150,y=20)
    linea2 = tk.Frame(frame, width=80, height=2, bg='black').place(x=170, y=52)
    
    user1 = customtkinter.CTkEntry(master=frame, placeholder_text='Username', width=250, height= 35, corner_radius=4)
    user1.place(x=80,y=100)

    password = customtkinter.CTkEntry(master=frame, placeholder_text='🔒 Password', width=250, height= 35, corner_radius=4)
    password.place(x=80,y=160)
    passwordc = customtkinter.CTkEntry(master=frame, placeholder_text='🔒 Confirm Password', width=250, height= 35, corner_radius=4)
    passwordc.place(x=80,y=220)
    
    #checkbox = customtkinter.CTkCheckBox(master=frame, text="Accept Terms and Conditions", width=10, height= 10, corner_radius=5)
    #checkbox.place(x=80,y=320)

    register = tk.Button(frame,width=20,pady=7,text='Register', bg='#BD81EB', fg='white', border=0, command= Verify).place(x=130, y=400)
    
p_signin()




#p_signin()

APP.mainloop()
#__________________________________________________________________________________________________________