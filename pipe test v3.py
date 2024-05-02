import os

try:
    import glfw
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
except ImportError:
    os.system('pip3 install PyOpenGL PyOpenGL_accelerate glfw')
    import glfw
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *

# Define rotations
x_rotation = 0.0
y_rotation = 0.0

def initialize_window():
    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "3D Pipe", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)  # Enable depth test

    return window

def set_color(color):
    glColor3f(*color)

def key_callback(window, key, scancode, action, mods):
    global x_rotation, y_rotation

    if action == glfw.PRESS:
        if key == glfw.KEY_W:
            x_rotation += 5.0
        elif key == glfw.KEY_S:
            x_rotation -= 5.0
        elif key == glfw.KEY_A:
            y_rotation += 5.0
        elif key == glfw.KEY_D:
            y_rotation -= 5.0

def draw_pipe(radius=0.25, thickness=0.05, height=1, num_slices=64, num_stacks=64):
    quadric = gluNewQuadric()

    for i in range(num_stacks):
        set_color((i/num_stacks, 1 - i/num_stacks, 0))  # Set a different color for each segment
        draw_segment(radius, thickness, height/num_stacks, num_slices, quadric)
        glTranslatef(0, 0, height/num_stacks)

def draw_segment(radius, thickness, height, num_slices, quadric):
    gluCylinder(quadric, radius, radius, height, num_slices, 1)
    gluCylinder(quadric, radius-thickness, radius-thickness, height, num_slices, 1)
    gluDisk(quadric, radius-thickness, radius, num_slices, 1)

def main():
    window = initialize_window()
    if not window:
        return

    glfw.set_key_callback(window, key_callback)

    # Setup perspective projection
    aspect_ratio = 640.0 / 480.0
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, aspect_ratio, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()
    gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)
        glRotatef(x_rotation, 1, 0, 0)
        glRotatef(y_rotation, 0, 1, 0)

        draw_pipe()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
