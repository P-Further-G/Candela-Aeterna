from pyglet.gl import *
from Moduleq.GlobalVariables import *
from Moduleq.Writer import *
from Moduleq.Shader import Shaderq
from Moduleq.VertexArrayIndexBuffer import Obje


config  = Config(sample_buffers = 1,
                 samples        = 4, 
                 depth_size     = 24, 
                 double_buffer  = True)

win = pyglet.window.Window(Width, Height, Title,
                           resizable = True,
                           vsync     = False,
                           config    = config)


keys        = pyglet.window.key.KeyStateHandler()
fps_display = pyglet.window.FPSDisplay(window=win)

glEnable(GL_DEPTH_TEST)
glEnable(GL_CULL_FACE)

win.set_minimum_size(500,300)
win.push_handlers(keys)
glClearColor(0.1,0.1,0.1,1.0)

poz =  [
-1,-1,-10,
-1, 1,-10,
 1,-1,-10,
 1, 1,-10,
-1,-1, -5,
-1, 1, -5,
 1,-1, -5,
 1, 1, -5 
]

ind = [
0,1,2,
2,1,3,

0,4,1,
4,5,1,

4,6,5,
5,6,7,

2,3,6,
6,3,7,

1,5,3,
5,7,3,

0,2,4,
4,2,6
]

tex = [
0,0,
0,1,
1,0,
1,1,
0,0,
0,1,
1,0,
1,1
]

normals = [
0,0,0,
0,0,0,
0,0,0,
0,0,0,
0,0,0,
0,0,0,
0,0,0,
0,0,0
]

cube = Obje(poz,ind,tex,normals)

project = pyglet.math.Mat4.perspective_projection(Width/float(Height),z_near=z_Near, z_far=z_Far)
mwm = pyglet.math.Mat4([ 1.0, 0.0, 0.0, 0.0,
                        0.0, 1.0, 0.0, 0.0,
                        0.0, 0.0, 1.0, 0.0,
                        0.0, 0.0, 0.0, 1.0])

shaderp = Shaderq('Shaders/VertexShader.shader','Shaders/FragmentShader.shader',project,mwm)


#pyglet.math.Mat4.orthogonal_projection(0,Width,0,Height,-1,1)

@win.event
def on_resize(width, height):

    global Height, Width

    Width = width
    Height = height

    glViewport(0, 0, *win.get_framebuffer_size())

    return pyglet.event.EVENT_HANDLED 

@win.event
def on_draw():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    
    shaderp.program.use()
    vlist = shaderp.program.vertex_list_indexed(int(len(poz)/3), GL_TRIANGLES, ind, position=('f',(poz)),
                                                                                    normal=('f',(normals)),
                                                                                    texcoord=('f',(tex)))
    vlist.draw(GL_TRIANGLES)

    


    fps_display.draw()

#pyglet.clock.schedule_interval(update, 1.0/Fps)

pyglet.app.run(interval= 1.0/Fps)


           
