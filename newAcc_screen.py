import customtkinter
import tkinter
import login_screen
from verifications import User
from tkinter import messagebox
from add_data import Data

def back_to_login_screen(frame):
    frame.destroy()
    login_screen.login()


def erro_message(msg):
    return messagebox.showinfo('Tente Novamente', f'{msg}')


def add_data_user(username, password, email, user_type):
    data_user = Data(username, password, email, user_type)
    data_user.add_username_on_names_list()
    data_user.creat_client_file()
    data_user.add_data_on_client_file()



def newAcc_class_instance(username, password, email, user_type):
    newAcc_instance = User(username,password,email,user_type)

    if newAcc_instance.verify_username_on_names_file() == True:
            erro_message('Usuário já cadastrado')
    else:
        add_data_user(username, password, email, user_type)
        messagebox.showinfo('Parabéns', 'Conta criada com sucesso !! Faça o Login !!')


def new_account():

    #========== Creating a frame for inputs
    new_account_frame = customtkinter.CTkFrame()
    new_account_frame.pack(pady=20, padx=60, fill="both", expand=True)


    # ========== Welcome start message 
    welcome_text = tkinter.Label(master=new_account_frame ,text='Registre-se', font='Arial 30', fg='white', bg='#2A2D2E')
    welcome_text.pack(pady=12, padx=10)


    # ========== Radios Inputs
    new_user_var = tkinter.StringVar()

    add_barber = customtkinter.CTkRadioButton(master=new_account_frame ,variable=new_user_var, value='barber', text='Sou Barbeiro')
    add_barber.pack(pady=12, padx=10)

    add_client = customtkinter.CTkRadioButton(master=new_account_frame ,variable=new_user_var, value='client', text='Sou Cliente    ')
    add_client.pack(pady=12, padx=10)


    # ========== Data Inputs
    add_name_entry = customtkinter.CTkEntry(master=new_account_frame, placeholder_text='Novo Usuário', width=200)
    add_name_entry.pack(pady=12, padx=10)

    add_email_entry = customtkinter.CTkEntry(master=new_account_frame, placeholder_text='Novo Email', width=200)
    add_email_entry.pack(pady=12, padx=10)


    add_password_entry = customtkinter.CTkEntry(master=new_account_frame, placeholder_text='Nova Senha', width=200, show="*")
    add_password_entry.pack(pady=12, padx=10)


    add_account_button = customtkinter.CTkButton(master=new_account_frame, text='Criar Conta', width=200, command=lambda: newAcc_class_instance(add_name_entry.get(), add_password_entry.get(), add_email_entry.get(), new_user_var.get()))
    add_account_button.pack(pady=12, padx=10)

    back_login_button = customtkinter.CTkButton(master=new_account_frame, text='Fazer Login', width=200, command=lambda: back_to_login_screen(new_account_frame))
    back_login_button.pack()
