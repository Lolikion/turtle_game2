from tkinter import *

mn=Tk()
canvas = Canvas(mn,width = 200, height = 200, bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)
image=PhotoImage(file = "C://Users//Houjo//PycharmProjects//turtle_game//pics//bg1.png")
canvas.create_image(10, 10, image = image, anchor = NW)
mn.mainloop()

# bg = PhotoImage(file="Your_img.png")
#
# # Create Canvas
# canvas1 = Canvas(root, width=400,
#                  height=400)
#
# canvas1.pack(fill="both", expand=True)
#
# # Display image
# canvas1.create_image(0, 0, image=bg,
#                      anchor="nw")