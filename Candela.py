import pyglet
from pyglet.gl import *
from Moduleq.Writer import Text
from Moduleq.Shader import Shaderq
from Moduleq.Scene import Scene


config  = Config(sample_buffers = 1,
                 samples        = 4, 
                 depth_size     = 16, 
                 double_buffer  = True)


win = pyglet.window.Window(1280, 620, "Candela Aeterna",
                           resizable = True,
                           vsync     = True,
                           config    = config)


keys        = pyglet.window.key.KeyStateHandler()
fps_display = pyglet.window.FPSDisplay(window=win)


glEnable(GL_DEPTH_TEST)
glEnable(GL_CULL_FACE)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glDepthFunc(GL_LEQUAL)

win.set_minimum_size(500,300)
win.push_handlers(keys)
glClearColor(0.1,0.1,0.1,1.0)


ShaderProgram = Shaderq('Shaders/VertexShader.shader','Shaders/FragmentShader.shader')
Sahne = Scene(ShaderProgram)
Sahne.visible = False

Sahne2 = Scene(ShaderProgram)
Sahne2.delete_obj('def')


foto = pyglet.image.load('resources/menü.png')


Sahne2.add_sprite('1',foto,0.0, 0.0, 0.4, 0.6)


def huh():

    Sahne.flip_visiblity()
    Sahne2.flip_visiblity()
    print("aa")


Sahne2.add_button('ney1',0.0, 0.0, 0.4, 0.6, huh)





@win.event
def on_resize(width, height):

    glViewport(0,0, *win.get_framebuffer_size())

    ShaderProgram.projection = pyglet.math.Mat4.perspective_projection(width/float(height),z_near=0.1, z_far=255,fov=60.0)
    ShaderProgram.program['projection'] = ShaderProgram.projection

    win.projection = pyglet.math.Mat4.orthogonal_projection(0,width,0,height, -1,1)

    Sahne2.scale_acc_to_window(width,height)

    return pyglet.event.EVENT_HANDLED 




@win.event
def on_mouse_press(x, y, button, modifiers):

    Sahne2.click_event(win,x,y)



@win.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):

    if ShaderProgram.is_on: ShaderProgram.Transform(0,0,scroll_y)




@win.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & pyglet.window.mouse.LEFT & ShaderProgram.is_on:
        ShaderProgram.rotate(dy/100, -dx/100)




@win.event
def on_draw():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    ShaderProgram.program.use()
    
    Sahne.render()
    Sahne2.render()
    
    fps_display.draw()




def update(dt):

    pass



if __name__ == '__main__':

    #pyglet.clock.schedule_interval(update, 1.0/120.0)
    pyglet.app.run(interval = 1.0/120.0)


           
