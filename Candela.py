import pyglet
from pyglet.gl import *
from Moduleq.Writer import Text
from Moduleq.Camera import Camera
from Moduleq.Scene import Scene
from LevelEditor import Level



config  = Config(sample_buffers = 1,
                 samples        = 4, 
                 depth_size     = 16, 
                 double_buffer  = True)


win = pyglet.window.Window(1280, 620, "Candela Aeterna",
                           resizable = True,
                           vsync     = True,
                           config    = config)


fps_display = pyglet.window.FPSDisplay(window=win)


glEnable( GL_DEPTH_TEST )
glEnable( GL_CULL_FACE  )
glEnable(   GL_BLEND    )
glEnable( GL_TEXTURE_2D )

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glDepthFunc(GL_LEQUAL)

win.set_minimum_size(500,300)

glClearColor(0.1,0.1,0.1,1.0)

engine = Level(win)




@win.event
def on_resize(width, height):

    glViewport(0,0, *win.get_framebuffer_size())

    engine.resize(width,height)
    engine.scale(width,height)

    win.projection = pyglet.math.Mat4.orthogonal_projection(0,width,0,height, -1,1)


    return pyglet.event.EVENT_HANDLED 




@win.event
def on_mouse_press(x, y, button, modifiers):

    engine.on_click(x,y)




@win.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):

    engine.on_scroll(scroll_y)




@win.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):

    if buttons & pyglet.window.mouse.LEFT: engine.on_drag(dx,dy)




@win.event
def on_draw():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    engine.show()
    
    fps_display.draw()




def update(dt):

    engine.on_update(dt)




if __name__ == '__main__':

    pyglet.clock.schedule_interval(update, 1.0/120.0)
    pyglet.app.run(interval = 1.0/120.0)


           
