import customtkinter
from tkinter import Label
from tkinter import StringVar
from tkinter import messagebox
import login_screen


# BACKUP CLIENT SCREEN

def exit_section(frame):
    frame.destroy()
    login_screen.login()


def add_clients_to_barber_file(barber_name,client_name,time_selected):
    barber_client_file = open(f'database/barber_data/{barber_name}_clients.txt', 'a')
    barber_client_file.write(f'{client_name} ------ {time_selected}\n')
    barber_client_file.close()
    messagebox.showinfo('Parabéns', f'Horário agendado ás {time_selected} com {barber_name}')

    

def barber_selected_frame(barber_name,frame,client_name):
    barber_file = open(f'database/barber_data/{barber_name}.txt', 'r')
    barber_file_list = barber_file.readlines()

    print(barber_file_list)
    print(len(barber_file_list))

    barber_file_formated = []

    e = 2
    while e < len(barber_file_list):
        barber_file_formated.append(barber_file_list[e])
        e = e + 1
    print(barber_file_formated)


    new = []
    for x in barber_file_formated:
        item = x
        for y in ['\n']:
            item = item.replace(y, "")
            new.append(item)
    print(new)

    times_barber_combobox_variable = StringVar()

    times_barber_combobox = customtkinter.CTkComboBox(master=frame,values=new, width=200, variable=times_barber_combobox_variable)
    times_barber_combobox.pack(pady=22, padx=10)

    select_time_button = customtkinter.CTkButton(master=frame, text='Confirmar Horário', width=200, fg_color='#22AED1', command=lambda: add_clients_to_barber_file(barber_name,client_name,times_barber_combobox_variable.get()))
    select_time_button.pack(pady=22, padx=10)

    exit_button = customtkinter.CTkButton(master=frame, text='Finalizar Sessão',width=200, fg_color='#B11E00', command=lambda: exit_section(frame))
    exit_button.pack(pady=12, padx=10)






def client_screen_home():
    client_frame = customtkinter.CTkFrame()
    client_frame.pack(pady=20, padx=60, fill="both", expand=True)

    #========== Welcome message
    welcome_message = Label(master=client_frame, text=f'Selecione o Barbeiro', font='Arial 30',fg='white', bg='#2A2D2E')
    welcome_message.pack(pady=12, padx=10)


    #========== Buttons 
    barbers_list = open(f'database/barber_data/barber_list.txt' ,'r')

    new = []
    for x in barbers_list.readlines():
        item = x
        for y in ['\n']:
            item = item.replace(y, "")
            new.append(item)
    barbers_list.close()
    

    selected_barber_variable = StringVar()

    barbers_list_combobox = customtkinter.CTkComboBox(master=client_frame,values=new, width=200, variable=selected_barber_variable)
    barbers_list_combobox.pack()

    client_name_confirm = customtkinter.CTkEntry(master=client_frame, placeholder_text='Confirme Cliente', width=200)
    client_name_confirm.pack(pady=12, padx=10)

    select_barber_button = customtkinter.CTkButton(master=client_frame, text='Selecionar', width=200, command=lambda: barber_selected_frame(selected_barber_variable.get(),client_frame, client_name_confirm.get()))
    select_barber_button.pack(pady=12, padx=10)