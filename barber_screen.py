import customtkinter
from tkinter import Label
from tkinter import messagebox
import login_screen

class Barber:


    def exit_section(frame):
        frame.destroy()
        login_screen.login()

    
    def confirm_client_service(barber_name,check_list):
        barber_client_file = open(f'database/barber_data/{barber_name}_clients.txt', 'r')
        barber_client_list = barber_client_file.readlines()

        new = []
        for x in barber_client_list:
            item = x
            for y in ['\n']:
                item = item.replace(y, "")
                new.append(item)

        for check in check_list:
            if check.check_state == True:
                position = check_list.index(check)
                del new[position]
        barber_client_file.close()

        barber_clients_stayed = open(f'database/barber_data/{barber_name}_clients.txt', 'w')
        for stayed_client in new:
            barber_clients_stayed.write(f'{stayed_client}\n')
        barber_clients_stayed.close()

        messagebox.showinfo('Parabéns', 'Cliente Atendido com Sucesso, Finalize a Sessão !!')
        


        
  

    @classmethod
    def see_scheduled_clients(cls,frame,username):
        frame.destroy()
        see_clients_frame = customtkinter.CTkFrame()
        see_clients_frame.pack(pady=20, padx=60, fill="both", expand=True)

        message = Label(see_clients_frame, text='Clientes Agendados',fg='white', bg='#2A2D2E', font='Arial 30')
        message.pack(pady=12, padx=10)

        message2 =  Label(see_clients_frame, text='<Selecione 1 cliente por vez>',fg='white', bg='#2A2D2E', font='Arial 10')
        message2.pack(pady=12, padx=10)

        barber_file = open(f'database/barber_data/{username}_clients.txt', 'r')

        clients_list = barber_file.readlines()
        checkbox_clients_list = []

        for client in clients_list:
            checkbox = customtkinter.CTkCheckBox(master=see_clients_frame, text=f'{client}')
            checkbox.pack(pady=12, padx=10)
            checkbox_clients_list.append(checkbox)

        

        barber_file.close()

        confirm_client_button = customtkinter.CTkButton(master=see_clients_frame, text='Confirmar Atendimento',width=200,command=lambda: cls.confirm_client_service(username,checkbox_clients_list))
        confirm_client_button.pack(pady=12, padx=10)
         
        exit_button = customtkinter.CTkButton(master=see_clients_frame, text='Finalizar Sessão',width=200, fg_color='#B11E00', command=lambda: cls.exit_section(see_clients_frame))
        exit_button.pack(pady=12, padx=10)



    @staticmethod
    def add_schedules_function(checkbox_1, checkbox_2,checkbox_3,checkbox_4,checkbox_5, barber_name):
        times_checkbox = [checkbox_1, checkbox_2,checkbox_3,checkbox_4,checkbox_5]

        barber_file = open(f'database/barber_data/{barber_name}.txt', 'a')

        for state in times_checkbox:
            if state.check_state == True:
                barber_file.write(f'\n{state.text}')
        messagebox.showinfo('Parabéns', 'Horários Adicionados com sucesso')
        barber_file.close()




    @classmethod
    def add_schedules_screen(cls,home_frame):
        home_frame.destroy()

        add_schedules_frame = customtkinter.CTkFrame()
        add_schedules_frame.pack(pady=20, padx=60, fill="both", expand=True)

        #========== Message
        message = Label(master=add_schedules_frame, text=f'Adicionar Horários de Atendimento', font='Arial 20',fg='white', bg='#2A2D2E')
        message.pack(pady=12, padx=10)

        #========== Time's checkbox
        checkbox_1 = customtkinter.CTkCheckBox(master=add_schedules_frame, text="8:00")
        checkbox_1.pack(pady=12, padx=10)


        checkbox_2 = customtkinter.CTkCheckBox(master=add_schedules_frame, text="9:00")
        checkbox_2.pack(pady=12, padx=10)

        checkbox_3 = customtkinter.CTkCheckBox(master=add_schedules_frame, text="10:00")
        checkbox_3.pack(pady=12, padx=10)

        checkbox_4 = customtkinter.CTkCheckBox(master=add_schedules_frame, text="11:00")
        checkbox_4.pack(pady=12, padx=10)

        checkbox_5 = customtkinter.CTkCheckBox(master=add_schedules_frame, text="12:00")
        checkbox_5.pack(pady=12, padx=10)

        barber_name_confirm = customtkinter.CTkEntry(master=add_schedules_frame, placeholder_text='Confirme o Usuário', width=200)
        barber_name_confirm.pack(pady=12, padx=10)

        add_schedules_button = customtkinter.CTkButton(master=add_schedules_frame, text='Adicionar Horários',width=200, command=lambda: cls.add_schedules_function(checkbox_1, checkbox_2,checkbox_3,checkbox_4,checkbox_5,barber_name_confirm.get()))
        add_schedules_button.pack(pady=12, padx=10)

        exit_button = customtkinter.CTkButton(master=add_schedules_frame, text='Finalizar Sessão',width=200, fg_color='#B11E00', command=lambda: cls.exit_section(add_schedules_frame))
        exit_button.pack(pady=12, padx=10)




    @classmethod 
    def barber_screen_home(cls, username):
        home_frame = customtkinter.CTkFrame()
        home_frame.pack(pady=20, padx=60, fill="both", expand=True)

        #========== Welcome message
        welcome_message = Label(master=home_frame, text=f'Bem-Vindo', font='Arial 30',fg='white', bg='#2A2D2E')
        welcome_message.pack()


        #========== Buttons 
        add_schedules_button = customtkinter.CTkButton(master=home_frame, text='Adicionar Horários de Atendimento',width=300, command=lambda: cls.add_schedules_screen(home_frame))
        add_schedules_button.pack(pady=12, padx=10)

        see_scheduled_clients_button = customtkinter.CTkButton(master=home_frame, text='Ver Clientes Agendados',width=300, command=lambda: cls.see_scheduled_clients(home_frame,username))
        see_scheduled_clients_button.pack(pady=12, padx=10)

        exit_button = customtkinter.CTkButton(master=home_frame, text='Finalizar Sessão',width=300, fg_color='#B11E00', command=lambda: cls.exit_section(home_frame))
        exit_button.pack(pady=12, padx=10)