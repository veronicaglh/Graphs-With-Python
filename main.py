# This project will be able to draw the graphs of two mathematical functions at the same time.
# The graph of one function will be drawn with purple color while the other one will be drawn with yellow color
# It will also display a UI that will let users chose which graph to be drawn
# The UI will be built using tkinter
# For this project to work it is important to install the following packages.
# To install packages execute the commands given below in your IDE terminal.
# pip install PyOpenGL PyOpenGL_accelerate
# pip install glfw
# pip install pygame
# pip install numpy
# pip install pillow
# pip install PyOpenGL PyOpenGL_accelerate

# Import Statements 
import numpy as np
from PIL import Image, ImageTk
import pygame
from tkinter import *
from tkinter import messagebox
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

# Making the input entry field for user to input function of their choice
usersFunction = Entry(myWindow, width=30, border=3)
usersFunction.place(x=90, y=490)

# Now, all we are left with the tkinter part is  the "generate graph" button.
# However we can not implement the button here. Why? Because when the button is clicked it will call the MAIN() function.
# But the main function has not been written yet so the button has to be implemented after the main function is written


# PART II - COMPUTATION
# Computation of how the graph of the functions will be drawn once button is clicked
# Y and Z need to be global so that we can access them in the draw function later
global y
global z
global event


def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


# There are many ways to implement the DRAW() function
# We could write a main function and a draw function for each pair of functions
# In other words one draw function for A, another for B and  another for C
# But its better if we don't repeat ourselves (DRY principle)
# So chose to have one main and one draw function
# the userFunction.get() method will read what the user has entered in the input field
# if the user entered A it will assign the appropriate function to y and z.
# Same thing for other inputs ,like B and C,of the user
# after assigning the functions y and z appropriately it will then implement the code


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    x = np.linspace(-1, 1, 100)
    if usersFunction.get() == "A":
        y = np.sin(x)
        z = np.cos(x)
    elif usersFunction.get() == "B":
        y = np.power(x, 3)
        z = np.power(x, 4)
    elif usersFunction.get() == "C":
        y = np.power(x, 2)
        z = np.tan(x)
    glPointSize(10)
    glBegin(GL_LINE_STRIP)
    # for every pair (a, b) of the numbers in x, y
    for a, b in zip(x, y):
        # giving (a, b) to OpenGL to draw
        glVertex2f(a, b)
        glColor3f(1.0, 0.0, 1.0)  # y(x) will be purple
    for c, d in zip(x, z):
        glVertex2f(c, d)
        glColor3f(1.0, 1.0, 0.0)  # z(x) will be Yellow
    glEnd()
    glFlush()


def main():
    # Will only call the draw and init function if the user enters appropriate value(A B or C)
    if usersFunction.get() == "A" or usersFunction.get() == "B" or usersFunction.get() == "C":
        init()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            draw()
            pygame.display.flip()
            pygame.time.wait(10)

    # If the user enters inappropriate value this will be printed on warning message box
    elif usersFunction.get() != "A" or usersFunction.get() != "B" or usersFunction.get() != "C":
        def popup():
            messagebox.showwarning("Warning Message", "Sorry you can only chose a function from the given pairs. Please enter either: A B or C ")
        popup()


# Lets get back to that tkinter generate graph button
# Tkinter "generate graph" Button
generator = Button(myWindow, text="Generate Graph", font="Calibri 8 italic", command=main)
generator.place(x=195, y=520)
myWindow.mainloop()