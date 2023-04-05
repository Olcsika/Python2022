# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("1000x1050")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300)
canvas.pack()

# Add a line in canvas widget
canvas.create_line(100,100,300,100, fill="green", width=5)
canvas.create_line(100,100,60,200, fill="green", width=5)
canvas.create_line(300,100,340,200, fill="green", width=5)
canvas.create_line(60,200,60,500, fill="green", width=5)
canvas.create_line(340,200,340,500, fill="green", width=5)
canvas.create_line(60,500,100,600, fill="green", width=5)


win.mainloop()
