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
except ImportError:
    os.system('pip3 install PyOpenGL PyOpenGL_accelerate glfw pygame')
    import glfw
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from pygame.locals import *
    import pygame

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
def main():
    
    pressed = [False, False, False, False, False]
    x_rotation = 0
    y_rotation = 0
    
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    glOrtho(-2, 2, -2, 2, 0.1, 50.0)  # Setting Orthographic projection
    
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
            if event.type == pygame.KEYUP and pressed[0]:
                pressed[0] = False
                pressed[1] = False
                pressed[2] = False
                pressed[3] = False
                pressed[4] = False

        if pressed[1]:
            x_rotation += 5.0
        if pressed[2]:
            x_rotation -= 5.0
        if pressed[3]:
            y_rotation += 5.0
        if pressed[4]:
            y_rotation -= 5.0
        
        glLoadIdentity()
        glRotatef(x_rotation, 1, 0, 0)
        glRotatef(y_rotation, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
