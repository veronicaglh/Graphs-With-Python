# This project will be able to draw the graphs of two mathematical functions at the same time.
# The graph of one function will be drawn with purple color while the other one will be drawn with yellow color
# It will also display a UI that will let users chose which graph to be drawn
# The UI will be built using tkinter
# For this project to work it is important to install the following packages.
# To install packages use write the commands given below in your IDE terminal.
# pip install PyOpenGL PyOpenGL_accelerate
# pip install glfw
# pip install pygame
# pip install numpy
# pip install pillow
# pip install PyOpenGL PyOpenGL_accelerate

import numpy as np
from PIL import Image, ImageTk
import pygame
from tkinter import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import PIL.Image

# PART I - TKINTER GUI
myWindow = Tk()
myWindow.title("Computer Graphics")
myWindow.geometry('563x789')
myWindow['background'] = '#BE8C5B'

load = PIL.Image.open('Image\\tkinterBackground.jpg')
render = ImageTk.PhotoImage(load)
img = Label(myWindow, image=render)
img.place(x=0, y=0)

title1 = Label(myWindow, text="Welcome to Graphopedia", bg="#F5C5B9", font="Calibri 20 bold")
title2 = Label(myWindow, text="Where you can see the graph of two functions", bg="#F5C5B9", font="Calibri 10 italic")

title3a = Label(myWindow, text="Please chose one of the following pairs", bg="#F5C5B9", font="Calibri 10 italic")
title3b = Label(myWindow, text="of functions to be drawn:", bg="#F5C5B9", font="Calibri 10 italic")

title4a = Label(myWindow, text="A. y=sin(x) and z=cos(x)", bg="#F5C5B9", font="Calibri 10 bold")
title4b = Label(myWindow, text="B. y=x^3 and z=x^4", bg="#F5C5B9", font="Calibri 10 bold")
title4c = Label(myWindow, text="C.y=x^2 and z=tan(x)", bg="#F5C5B9", font="Calibri 10 bold")

title5a = Label(myWindow, text="In the input field below enter either A or B or C", bg="#F5C5B9", font="Calibri 10 italic")
title5b = Label(myWindow, text="**A, B or C must be capital and have no other punctuation", bg="#F5C5B9", font="Calibri 8 italic")
title5c = Label(myWindow, text="**The y func will be purple and the z func will be yellow ", bg="#F5C5B9", font="Calibri 8 italic")

title1.place(x=110, y=180)
title2.place(x=130, y=220)
title3a.place(x=90, y=300)
title3b.place(x=90, y=320)
title4a.place(x=100, y=355)
title4b.place(x=100, y=375)
title4c.place(x=100, y=395)
title5a.place(x=90, y=430)
title5b.place(x=90, y=450)
title5c.place(x=90, y=470)


myWindow.mainloop()