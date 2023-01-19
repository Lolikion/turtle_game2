#TODO
# settings -> controls
# Inventory -> items
# Pause button
# Localisation
# Cameras)))))
from time import strftime
from tkinter import *
from tkinter import ttk

inv=1 #num of standart invertory cell
hp=19
table_state=0


def open_game():
    global menu_window,menu_frm,h
    menu_frm.grid_forget()
    game_screen.grid()
    game_screen.create_image(0, 0, image=hp_bar, anchor=NW)
    game_screen.create_image(100, h-200, image=invertory, anchor=NW)
    game_screen.create_image(w-400, h - 300, image=tablet_closed, anchor=NW)
    tablet_time.place(x=w-370,y=h-280,width=80,height=20)
    change_time()


def change_time():
    tablet_time.configure(text=strftime("%H:%M:%S"))
    tablet_time.after(1000,change_time)


def open_oz():
    global oz_obj
    oz_obj = game_screen.create_image(0, 0, image=oz1, anchor=NW)
    tablet_time.place_forget()
    return oz_obj


def change_tablet():
    global table_state,game_screen,tablet_time
    if table_state==0:
        open_oz()
        table_state = 1
    elif table_state==1:
        game_screen.delete(oz_obj)
        tablet_time.place(x=w-370,y=h-280,width=80,height=20)
        table_state=0


def pause():
    global pause_frm
    pause_frm.grid()
    print(228)

def key_press(event):
    global inv,invertory,menu_window
    if event.keysym in '1234':
        inv=int(event.keysym)
        invertory.configure(file = f"C://Users//Houjo//PycharmProjects//turtle_game//pics//invertory//inv{inv}.png")
    elif event.keysym=='space':
        change_tablet()
    elif event.keysym=='Escape':
        pause()


def open_menu_from_settings():
    global settings_frm,menu_frm
    settings_frm.grid_forget()
    menu_frm.grid()


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
    global menu_frm,settings_frm,f,language_change
    menu_frm.grid_forget()
    settings_frm.grid()
    menu_button.place(relx=0.46, rely=0.6, relwidth=0.1)
    language_change.place(relx=0.46, rely=0.4, relwidth=0.1)
    controls_button.place(relx=0.46, rely=0.5, relwidth=0.1)
    language_change.bind('<<ComboboxSelected>>', change_language)

def open_settings_from_controls():
    global controls_frm,settings_frm,f,language_change
    controls_frm.grid_forget()
    settings_frm.grid()
    menu_button.place(relx=0.46, rely=0.6, relwidth=0.1)
    language_change.place(relx=0.46, rely=0.4, relwidth=0.1)
    controls_button.place(relx=0.46, rely=0.5, relwidth=0.1)
    language_change.bind('<<ComboboxSelected>>', change_language)


def open_controls():
    global settings_frm, controls_frm, settings_button2
    settings_frm.grid_forget()
    controls_frm.grid()
    settings_button2.place(relx=0.46, rely=0.6, relwidth=0.1)

# All widgets
menu_window = Tk()
w, h = menu_window.winfo_screenwidth(), menu_window.winfo_screenheight()
print(w,h)
menu_frm = ttk.Frame(menu_window,width=w,height=h)
settings_frm = ttk.Frame(menu_window, width=w, height=h)
controls_frm = ttk.Frame(menu_window, width=w, height=h)




menu_button = Button(settings_frm, text='Back to menu', command=open_menu_from_settings)
start_button=Button(menu_frm,text='Start game',command=open_game)
settings_button=Button(menu_frm,text='Settings',command=open_settings_from_menu)
settings_button2=Button(controls_frm,text='Settings',command=open_settings_from_controls)
language_change = ttk.Combobox(settings_frm,values=['English','Русский'])
exit_button=Button(menu_frm,text='Exit',command=menu_window.destroy)
controls_button=Button(settings_frm,text='Controls',command=open_controls)

game_screen = Canvas(menu_window,width = w, height = h, bg = 'blue')
game_bg=PhotoImage(file = "C://Users//Houjo//PycharmProjects//turtle_game//pics//backgrounds//bg1.png")
hp_bar=PhotoImage(file = f"C://Users//Houjo//PycharmProjects//turtle_game//pics//hpbar//hpbar_{hp}.png")
invertory=PhotoImage(file = f"C://Users//Houjo//PycharmProjects//turtle_game//pics//invertory//inv{inv}.png")
tablet_closed=PhotoImage(file = f"C://Users//Houjo//PycharmProjects//turtle_game//pics//tablet//tablet_closed.png")
oz1=PhotoImage(file = f"C://Users//Houjo//PycharmProjects//turtle_game//pics//tablet//tablet_opened1.png")

tablet_time=ttk.Label(game_screen)
pause_frm = ttk.Frame(game_screen, width=200, height=200)
pause_lbl = ttk.Label(pause_frm,text='lol')

# Use this to configure widgets
menu_window.attributes("-fullscreen", True)
menu_frm.grid()
start_button.place(relx=0.46,rely=0.4,relwidth=0.1)
settings_button.place(relx=0.46,rely=0.5,relwidth=0.1)
exit_button.place(relx=0.46,rely=0.6,relwidth=0.1)
language_change.current(0)
tablet_time.configure(text=strftime("%H:%M:%S:%p"),font=(30))
game_screen.create_image(0, 0, image = game_bg, anchor = NW)
menu_window.bind("<KeyPress>",key_press)

menu_window.mainloop()


