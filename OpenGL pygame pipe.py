import os
import sys

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

try:
    import glfw
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from pygame.locals import *
    import pygame
    import math
except ImportError:
    os.system('pip3 install PyOpenGL PyOpenGL_accelerate glfw pygame')
    import glfw
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from pygame.locals import *
    import pygame
    import math

verticies = ((0.5, -0.5, -0.5),
             (0.5, 0.5, -0.5),
             (-0.5, 0.5, -0.5),
             (-0.5, -0.5, -0.5),
             (0.5, -0.5, 0.5),
             (0.5, 0.5, 0.5),
             (-0.5, -0.5, 0.5),
             (-0.5, 0.5, 0.5))
edges = ((0,1),
         (0,3),
         (0,4),
         (2,1),
         (2,3),
         (2,7),
         (6,3),
         (6,4),
         (6,7),
         (5,1),
         (5,4),
         (5,7))

def ReadFile():
    global fileData
    if os.path.isfile('file.txt') is True:
        with open('file.txt', 'r') as file:
            data = file.read().replace('\n', '')
            fileData = list(data)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def XYZLines():
    global RED, GREEN, BLUE, WHITE
    glBegin(GL_LINES)
    glColor3fv(RED)
    glVertex3fv((0, 0, 0))
    glVertex3fv((0.5, 0, 0))
    glEnd()
    glBegin(GL_LINES)
    glColor3fv(GREEN)
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 0.5, 0))
    glEnd()
    glBegin(GL_LINES)
    glColor3fv(BLUE)
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 0, 0.5))
    glColor3fv(WHITE)
    glEnd()

def Pipe():
    global RED, GREEN, BLUE, WHITE, fileData
    radiusMax = 0.25
    radiusMin = 0.20
    thickness = 0.05
    height = 1
    slices = 16
    stacks = 1
    surrentStack = 0
    lastStack = 0
    pi = 3.141592653
    deltaAngle = pi / slices * 2
    angle = 0
    SquareSize = math.sin(pi / slices)
    xShift = SquareSize / 2
    yShift = 0
    zShift = 0

    for i in range(stacks):
        surrentStack = surrentStack + SquareSize
        xOut = 0
        yOut = 0
        xLastOut = 0
        yLastOut = 0
        glBegin(GL_QUADS)
        for i in range(slices):
            if fileData[i]:
                glColor3fv(RED)
            else:
                glColor3fv(GREEN)
            angle = angle + deltaAngle
            xOut = xOut + math.cos(angle) * SquareSize
            yOut = yOut + math.sin(angle) * SquareSize

            glVertex3fv((xLastOut + xShift, yLastOut + yShift, lastStack + zShift))
            glVertex3fv((xLastOut + xShift, yLastOut + yShift, surrentStack + zShift))
            glVertex3fv((xOut + xShift, yOut + yShift, surrentStack + zShift))
            glVertex3fv((xOut + xShift, yOut + yShift, lastStack + zShift))
            xLastOut = xOut
            yLastOut = yOut
        glEnd()
        lastStack = surrentStack

    glColor3fv(WHITE)

RED = (215 / 256, 10 / 256, 10 / 256)
GREEN = (40 / 256, 220 / 256, 70 / 256)
BLUE = (18 / 256, 47 / 256, 170 / 256)
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
fileData = []

def main():
    ReadFile()
    pressed = [False, False, False, False, False]
    x_rotation = 0
    y_rotation = 0
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not pressed[0]:
                    pressed[0] = True
                if event.key == pygame.K_w:
                    pressed[1] = True
                if event.key == pygame.K_s:
                    pressed[2] = True
                if event.key == pygame.K_a:
                    pressed[3] = True
                if event.key == pygame.K_d:
                    pressed[4] = True
                if event.key == pygame.K_ESCAPE:
                    x_rotation = 0
                    y_rotation = 0
            if event.type == pygame.KEYUP and pressed[0]:
                pressed[0] = False
                pressed[1] = False
                pressed[2] = False
                pressed[3] = False
                pressed[4] = False

        if pressed[1]:
            x_rotation += 2.0
        if pressed[2]:
            x_rotation -= 2.0
        if pressed[3]:
            y_rotation += 2.0
        if pressed[4]:
            y_rotation -= 2.0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        glRotatef(x_rotation, 1, 0, 0)
        glRotatef(y_rotation, 0, 1, 0)
        
        XYZLines()
        Pipe()
        #Cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
