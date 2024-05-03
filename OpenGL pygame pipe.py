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

verticies = (
    (0.5, -0.5, -0.5),
    (0.5, 0.5, -0.5),
    (-0.5, 0.5, -0.5),
    (-0.5, -0.5, -0.5),
    (0.5, -0.5, 0.5),
    (0.5, 0.5, 0.5),
    (-0.5, -0.5, 0.5),
    (-0.5, 0.5, 0.5)
    )
edges = (
    (0,1),
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
    (5,7)
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Pipe():
    p = 0.125
    d = 0.5
    num_slices = 24
    height = 1
    radius = 0.25
    GREEN = (0.18, 0.51, 0.27)
    glBegin(GL_QUADS)
    glColor3fv(GREEN)
    for surface in range(0, 24):
        glVertex3fv((p, -d, p))
        glVertex3fv((p, -d, -p))
        glVertex3fv((-p, -d, -p))
        glVertex3fv((-p, -d, p))

    for i in range(num_stacks):
        h = i / num_stacks
        top_color = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        bottom_color = colorsys.hsv_to_rgb(h + 0.1, 1.0, 1.0)

        glBegin(GL_QUAD_STRIP)
    
    for j in range(num_slices + 1):
            angle = j * 2 * 3.14159 / num_slices
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            glVertex3f(x, y, h * height)
            glVertex3f(x, y, (h + 1 / num_stacks) * height)
    glEnd()

def main():
    
    pressed = [False, False, False, False, False]
    x_rotation = 0
    y_rotation = 0
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
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
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -3)
        glRotatef(x_rotation, 1, 0, 0)
        glRotatef(y_rotation, 0, 1, 0)
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Pipe()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

##def draw_pipe(radius=0.25, thickness=0.05, height=1, num_slices=64, num_stacks=64):
##    quadric = gluNewQuadric()
##
##    for i in range(num_stacks):
##        h = i / num_stacks
##        top_color = colorsys.hsv_to_rgb(h, 1.0, 1.0)
##        bottom_color = colorsys.hsv_to_rgb(h + 0.1, 1.0, 1.0)
##
##        glBegin(GL_QUAD_STRIP)
##
##        for j in range(num_slices + 1):
##            angle = j * 2 * 3.14159 / num_slices
##            x = radius * math.cos(angle)
##            y = radius * math.sin(angle)
##
##            glColor3f(*top_color)
##            glVertex3f(x, y, h * height)
##
##            glColor3f(*bottom_color)
##            glVertex3f(x, y, (h + 1 / num_stacks) * height)
##
##        glEnd()
        #glLoadIdentity() is a function in pyOpenGL that resets the
        #current modelview matrix to the identity matrix. This means
        #that it effectively resets any transformations that have been
        #applied to the scene, essentially setting it back to its original state.
        #It is commonly used at the beginning of a drawing function to ensure
        #that the scene is drawn without any previous transformations affecting it.
