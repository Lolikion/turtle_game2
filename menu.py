from tkinter import *

ws=Tk()
ws.title('funny school)))')
ws.geometry('900x600+400-100')


def center(toplevel):
    toplevel.update_idletasks()
    # Tkinter way to find the screen resolution
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2
    toplevel.geometry("+%d+%d" % (x, y))

center(ws)
Button(ws,text='Start game').place(relx=.5, rely=.1,anchor= CENTER)
Button(ws,text='Settings').place(relx=.5, rely=.2,anchor= CENTER)
Button(ws,text='Exit',command=ws.destroy).place(relx=.5, rely=.3,anchor= CENTER)

ws.mainloop()

