from tkinter import *
from tkinter import ttk


def open_menu_from_settings():
    global f,frm1,frm
    f = 0
    frm1.grid_forget()
    frm.grid()


def change_language(event):
    global language_change,menu_button
    cur=language_change.get()
    if cur == 'Русский':
        menu_button.configure(text='Назад в меню')
        exit_button.configure(text='Выход')
        start_button.configure(text='Начать игру')
        settings_button.configure(text='Настройки')
        language_change.current(1)
    if cur == 'English':
        menu_button.configure(text='Back to menu')
        exit_button.configure(text='Exit')
        start_button.configure(text='Start game')
        settings_button.configure(text='Settings')
        language_change.current(0)


def open_settings_from_menu():
    global frm,frm1,f,language_change
    frm.grid_forget()
    frm1.grid()
    menu_button.place(relx=0.46, rely=0.6, relwidth=0.1)
    language_change.place(relx=0.46, rely=0.4, relwidth=0.1)
    language_change.bind('<<ComboboxSelected>>', change_language)

def start_game():
    pass

# All widgets
menu_window = Tk()
w, h = menu_window.winfo_screenwidth(), menu_window.winfo_screenheight()
frm = ttk.Frame(menu_window,width=w,height=h)
frm1 = ttk.Frame(menu_window, width=w, height=h)
menu_button = Button(frm1, text='Back to menu', command=open_menu_from_settings)
start_button=Button(frm,text='Start game')
settings_button=Button(frm,text='Settings',command=open_settings_from_menu)
language_change = ttk.Combobox(frm1,values=['English','Русский'])
exit_button=Button(frm,text='Exit',command=menu_window.destroy)


# Use this to configure widgets
menu_window.attributes("-fullscreen", True)
frm.grid()
start_button.place(relx=0.46,rely=0.4,relwidth=0.1)
settings_button.place(relx=0.46,rely=0.5,relwidth=0.1)
exit_button.place(relx=0.46,rely=0.6,relwidth=0.1)
language_change.current(0)
menu_window.mainloop()


