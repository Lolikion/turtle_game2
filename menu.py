#TODO
# settings -> controls
# Invertory -> items
# Pause button
# Localisation
import tkinter
from tkinter import *
from tkinter import ttk
inv=2
hp=19

def open_game():
    global menu_window,frm,gm1,h
    frm.grid_forget()
    game_screen.grid()
    menu_window.bind("<KeyPress>",key_press)
    game_screen.create_image(0, 0, image=hp_bar, anchor=NW)
    game_screen.create_image(100, h-200, image=invertory, anchor=NW)

def key_press(event):
    global inv,invertory
    if event.keysym in '1234':
        inv=int(event.keysym)
        invertory.configure(file = f"C://Users//Houjo//PycharmProjects//turtle_game//pics//invertory//inv{inv}.png")



def open_menu_from_settings():
    global frm1,frm
    frm1.grid_forget()
    frm.grid()


def change_language(event):
    global language_change
    cur=language_change.get()
    if cur == 'Русский':
        menu_button.configure(text='Назад в меню')
        exit_button.configure(text='Выход')
        start_button.configure(text='Начать игру')
        settings_button.configure(text='Настройки')
        settings_button2.configure(text='Настройки')
        controls_button.configure(text='Управление')
        language_change.current(1)
    if cur == 'English':
        menu_button.configure(text='Back to menu')
        exit_button.configure(text='Exit')
        start_button.configure(text='Start game')
        settings_button.configure(text='Settings')
        settings_button2.configure(text='Settings')
        controls_button.configure(text='Controls')
        language_change.current(0)


def open_settings_from_menu():
    global frm,frm1,f,language_change
    frm.grid_forget()
    frm1.grid()
    menu_button.place(relx=0.46, rely=0.6, relwidth=0.1)
    language_change.place(relx=0.46, rely=0.4, relwidth=0.1)
    controls_button.place(relx=0.46, rely=0.5, relwidth=0.1)
    language_change.bind('<<ComboboxSelected>>', change_language)

def open_settings_from_controls():
    global frm3,frm1,f,language_change
    frm3.grid_forget()
    frm1.grid()
    menu_button.place(relx=0.46, rely=0.6, relwidth=0.1)
    language_change.place(relx=0.46, rely=0.4, relwidth=0.1)
    controls_button.place(relx=0.46, rely=0.5, relwidth=0.1)
    language_change.bind('<<ComboboxSelected>>', change_language)


def open_controls():
    global frm1, frm3, settings_button2
    frm1.grid_forget()
    frm3.grid()
    settings_button2.place(relx=0.46, rely=0.6, relwidth=0.1)

# All widgets
menu_window=Tk()
w, h = menu_window.winfo_screenwidth(), menu_window.winfo_screenheight()



frm = ttk.Frame(menu_window,width=w,height=h)
frm1 = ttk.Frame(menu_window, width=w, height=h)
frm3 = ttk.Frame(menu_window, width=w, height=h)

menu_button = Button(frm1, text='Back to menu', command=open_menu_from_settings)
start_button=Button(frm,text='Start game',command=open_game)
settings_button=Button(frm,text='Settings',command=open_settings_from_menu)
settings_button2=Button(frm3,text='Settings',command=open_settings_from_controls)
language_change = ttk.Combobox(frm1,values=['English','Русский'])
exit_button=Button(frm,text='Exit',command=menu_window.destroy)
controls_button=Button(frm1,text='Controls',command=open_controls)

game_screen = Canvas(menu_window,width = w, height = h, bg = 'blue')
game_bg=PhotoImage(file = "C://Users//Houjo//PycharmProjects//turtle_game//pics//backgrounds//bg1.png")
hp_bar=PhotoImage(file = f"C://Users//Houjo//PycharmProjects//turtle_game//pics//hpbar//hpbar_{hp}.png")
invertory=PhotoImage(file = f"C://Users//Houjo//PycharmProjects//turtle_game//pics//invertory//inv{inv}.png")



# Use this to configure widgets


menu_window.attributes("-fullscreen", True)
frm.grid()
start_button.place(relx=0.46,rely=0.4,relwidth=0.1)
settings_button.place(relx=0.46,rely=0.5,relwidth=0.1)
exit_button.place(relx=0.46,rely=0.6,relwidth=0.1)
language_change.current(0)
game_screen.create_image(0, 0, image = game_bg, anchor = NW)


print(w,h)
menu_window.mainloop()


