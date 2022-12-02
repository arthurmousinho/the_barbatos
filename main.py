import tkinter
import tkinter.messagebox
import customtkinter
import login_screen

customtkinter.set_appearance_mode('Dark')

# ========== Settings of the Window
root = customtkinter.CTk()
root.geometry('1000x500')
root.title('The Barbatos')
icon = tkinter.PhotoImage(file='assets/icon.png')
root.iconphoto(False, icon)
root.command()


# ========== First frame to show
login_screen.login()
root.mainloop() 