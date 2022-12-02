import customtkinter
import tkinter
from verifications import User
from newAcc_screen import new_account
from tkinter import messagebox
from barber_screen import Barber
import client_screen 



def creat_account_screen(frame):
    frame.destroy()
    new_account()


def erro_message(msg):
    return messagebox.showinfo('Tente Novamente', f'{msg}')


def redirect_user_screen(frame,user_type,username):
    frame.destroy()
    if user_type == 'barber':
        barber_instance = Barber()
        barber_instance.barber_screen_home(username)

    elif user_type == 'client':
        client_screen.client_screen_home()
    else:
        pass


def login_class_instance(username, password, email, user_type,frame):
    user_instance = User(username,password,email,user_type)
    
    if user_instance.verify_username_on_names_file() == False:
        erro_message('Verfique seu usuário e tente novamente') 
    elif user_instance.verify_user_email() == False:
        erro_message('Verfique seu email e tente novamente')
    elif user_instance.verify_user_password() == False:
        erro_message('Verfique sua senha e tente novamente')
    else:
        redirect_user_screen(frame,user_type,username)


        

def login():
        # ========== Creating a frame for inputs
        main_frame = customtkinter.CTkFrame()
        main_frame.pack(pady=20, padx=60, fill="both", expand=True)


        message_begin = tkinter.Label(master = main_frame, text="Bem-Vindo ao The Barbatos", fg='white', bg='#2A2D2E', font='Arial 30')
        message_begin.pack(pady=12, padx=10)

        # ========== Radios Inputs
        type_of_user_var = tkinter.StringVar()

        barber_radiobutton = customtkinter.CTkRadioButton(master=main_frame, variable=type_of_user_var, value='barber', text='Sou Barbeiro')
        barber_radiobutton.pack(pady=12, padx=10)
        
        client_radiobutton = customtkinter.CTkRadioButton(master=main_frame, variable=type_of_user_var, value='client', text='Seu Cliente   ')
        client_radiobutton.pack(pady=12, padx=10)
        

        # ========== Data Inputs
        name_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text='Usuário', width=200)
        name_entry.pack(pady=12, padx=10)

        email_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text='Email', width=200)
        email_entry.pack(pady=12, padx=10)

        password_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text='Senha', width=200, show="*")
        password_entry.pack(pady=12, padx=10)


        login_button = customtkinter.CTkButton(master=main_frame, text='Fazer Login',width=200 ,command= lambda: login_class_instance(name_entry.get(),password_entry.get(), email_entry.get(), type_of_user_var.get(), main_frame))
        login_button.pack(pady=12, padx=10)


        creatAcc_button = customtkinter.CTkButton(master=main_frame, text='Criar Conta', width=200,command= lambda: creat_account_screen(main_frame))
        creatAcc_button.pack()
