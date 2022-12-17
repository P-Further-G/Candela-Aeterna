import pyglet
from Moduleq.Scene import Scene
from Moduleq.Camera import Camera

foto = pyglet.image.load('resources/menü.png')

class Level():

    def __init__(self,win):

        self.CURRENT_LEVEL = 0
        self.Camera = Camera('Shaders/VertexShader.shader','Shaders/FragmentShader.shader')
        self.window = win

    #=============================================================>

        self.menu = Scene(self.Camera)
        self.menu.delete_obj('def')
        self.menu.add_button('tuttifurti',0.47,0.47,0.53,0.53,self._openlvl1)
        self.menu.active = True
        self.menu.visible = True
        self.menu.add_sprite('ehe',foto,0.47,0.47,0.53,0.53)

        self.kup1 = Scene(self.Camera)

    #=============================================================>


    def resize(self,width,height):

        self.Camera.projection = pyglet.math.Mat4.perspective_projection(width/float(height),z_near=0.1, z_far=255,fov=60.0)
        self.Camera.program['projection'] = self.Camera.projection

    def scale(self,width,height):

        self.menu.scale_acc_to_window(width,height)

    def on_click(self,x,y):

         self.menu.click_event(self.window,x,y)

    def on_scroll(self,scroll_y):

        if self.Camera.is_on:
            self.Camera.will_move_to(self.Camera.pos_x, 
                                     self.Camera.pos_y,
                                     self.Camera.pos_z + 2*scroll_y)

    def on_drag(self,dx,dy):

        if self.Camera.is_on:
            self.Camera.will_rotate_to(self.Camera.angle_x + dy/10, self.Camera.angle_y + -dx/10)

    def on_update(self,dt):

        self.Camera.Smooth_Translate(5*dt)
        self.Camera.Smooth_Rotate(2*dt)


    #=============================================================>

    def show(self):

        if self.CURRENT_LEVEL == 0:

            self.Camera.program.use()
            self.menu.render()

        if self.CURRENT_LEVEL == 1:

            self.Camera.program.use()
            self.kup1.render()


    def _openlvl1(self):

        self.CURRENT_LEVEL = 1
        self.menu.visible = False
        self.menu.active = False
        self.kup1.active = True
        self.kup1.visible = True



    
