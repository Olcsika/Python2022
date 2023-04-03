# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x500+100+100")

# Create a canvas widget
canvas=Canvas(win, width=3000, height=3000,bg='black')
canvas.pack(fill = BOTH, expand = 1)

#canvas2=Canvas(win, width=3000, height=3000,bg='green')
#canvas2.pack()
# Add a line in canvas widget
canvas.create_line(100,200,200,35, fill="green", width=5)
canvas.create_line(200,100,200,35, fill="green", width=5)

win.mainloop()
