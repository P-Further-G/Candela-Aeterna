import pyglet
from pyglet.gl import *
from Moduleq.GlobalVariables import *
from Moduleq.Writer import *

options = WindowOptions()
config  = Config(sample_buffers = options.SampleBuffer,
                 samples        = options.Samples, 
                 depth_size     = options.DepthSize, 
                 double_buffer  = options.DoubleBuffer)

win = pyglet.window.Window(Width, Height, Title,
                           resizable = options.Resizable,
                           vsync     = options.Vsync,
                           config    = config)


keys        = pyglet.window.key.KeyStateHandler()
fps_display = pyglet.window.FPSDisplay(window=win)


win.set_minimum_size(500,300)
win.push_handlers(keys)
glClearColor(0.1,0.1,0.1,1.0)

met = "hee \n ney"


label = Text(met,30,Width/2,Height/2,[255,255,0,255],500)


@win.event
def on_resize(width, height):

    glViewport(0, 0, width, height)
    glMatrixMode(gl.GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(Fov, width / float(height), z_Near, z_Far)
    glMatrixMode(gl.GL_MODELVIEW)

    return pyglet.event.EVENT_HANDLED 


def update(dt):

    glClear(GL_COLOR_BUFFER_BIT)
    label.timed_draw(1,dt,win)
    fps_display.draw()

pyglet.clock.schedule_interval(update, 1.0/Fps)

pyglet.app.run()


           
