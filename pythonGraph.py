# This project will be able to draw the graphs of two mathematical functions at the same time.
# The graph of one function will be drawn with purple color while the other one will be drawn with yellow color
# It will also display a UI that will let users chose which graph to be drawn
# For this project to work it is important to install the following packages.
# To install packages use write the commands given below in your IDE'S terminal.
# pip install PyOpenGL PyOpenGL_accelerate
# pip install glfw
# pip install pygame
# pip install numpy
# pip install pillow
# pip install PyOpenGL PyOpenGL_accelerate

import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    # generate 100 points within -1 to 1 range
    x = np.linspace(-1, 1, 100)
    y = np.sin(x)
    z = np.cos(x)
    glPointSize(10)
    glBegin(GL_LINE_STRIP)
    # for every pair (a, b) of the numbers in x, y
    for a, b in zip(x, y):
    # give (a, b) to OpenGL to draw
        glVertex2f(a, b)
        glColor3f(1.0, 0.0, 1.0)

    for c, d in zip(x, z):
        glVertex2f(c, d)
        glColor3f(1.0, 1.0, 0.0)
    glEnd()
    glFlush()


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()
        pygame.display.flip()
        pygame.time.wait(10)
main()