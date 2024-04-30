import os

try:
    import glfw
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
    import numpy as np
except ImportError:
    os.system('pip3 install PyOpenGL PyOpenGL_accelerate glfw')
    os.system('pip3 install numpy')
    import glfw
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
    import numpy as np

# Define rotations
x_rotation = 0.0
y_rotation = 0.0

def initialize_window():
    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "3D Cube", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)  # Enable depth test

    return window

def key_callback(window, key, scancode, action, mods):
    global x_rotation, y_rotation

    if action == glfw.PRESS:
        if key == glfw.KEY_W:
            x_rotation -= 5.0
        elif key == glfw.KEY_S:
            x_rotation += 5.0
        elif key == glfw.KEY_A:
            y_rotation -= 5.0
        elif key == glfw.KEY_D:
            y_rotation += 5.0

def draw_cube():
    glBegin(GL_QUADS)

    # Front face
    glColor3f(1, 0, 0)  # Red
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    # Back face
    glColor3f(0, 1, 0)  # Green
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)

    # Top face
    glColor3f(0, 0, 1)  # Blue
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)

    # Bottom face
    glColor3f(1, 1, 0)  # Yellow
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)

    # Right face
    glColor3f(1, 0, 1)  # Magenta
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)

    # Left face
    glColor3f(0, 1, 1)  # Cyan
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    glEnd()

def main():
    window = initialize_window()
    if not window:
        return

    glfw.set_key_callback(window, key_callback)

    # Setup perspective projection
    aspect_ratio = 640.0 / 480.0  # Assuming a window size of 640x480 for simplicity
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, aspect_ratio, 0.1, 50.0)  # Field of view, aspect ratio, near clip, far clip
    glMatrixMode(GL_MODELVIEW)

    # Move the camera back a bit so we can see the cube
    glLoadIdentity()
    gluLookAt(0, 0, 3,  # Eye position (x, y, z)
              0, 0, 0,  # Center (x, y, z)
              0, 1, 0)  # Up vector (x, y, z)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Apply rotation
        glLoadIdentity()
        gluLookAt(0, 0, 3,  # Eye position (x, y, z)
                  0, 0, 0,  # Center position (x, y, z)
                  0, 1, 0)  # Up vector (x, y, z)
        glRotatef(x_rotation, 1, 0, 0)
        glRotatef(y_rotation, 0, 1, 0)

        draw_cube()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
