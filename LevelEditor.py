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
        self.menu.active = True
        self.menu.visible = True
        self.menu.add_button('tuttifurti',0.22,0.42,0.37,0.57,self._openlvl1)
        self.menu.add_sprite('ehe',foto,0.22,0.42,0.37,0.57)
        self.menu.add_button('tuttifurti2',0.62,0.42,0.77,0.57,self._openlvl2)
        self.menu.add_sprite('ehhe',foto,0.62,0.42,0.77,0.57)


        self.kup1 = Scene(self.Camera)
        self.kup1.add_object(self.kup1.getobj('ehe',[2,1,5,
                                                     0,5,0,
                                                     4,-2,-3],[0,1,2],[1,1,1,
                                                                       1,1,0,
                                                                       0,1,0],[0,0,
                                                                               1,1,
                                                                               0,1]))
        self.kup1.add_sprite('huh',foto,0.06,0.8,0.2,0.96)
        self.kup1.add_button('huuh',0.06,0.8,0.2,0.96,self._returntomenu)

        self.kup2 = Scene(self.Camera)
        self.kup2.add_sprite('huh',foto,0.06,0.8,0.2,0.96)
        self.kup2.add_button('huuh',0.06,0.8,0.2,0.96,self._returntomenu2)

    #=============================================================>


    def resize(self,width,height):

        self.Camera.projection = pyglet.math.Mat4.perspective_projection(width/float(height),z_near=0.1, z_far=255,fov=60.0)
        self.Camera.program['projection'] = self.Camera.projection

    def scale(self,width,height):

        self.menu.scale_acc_to_window(width,height)
        self.kup1.scale_acc_to_window(width,height)
        self.kup2.scale_acc_to_window(width,height)

    def on_click(self,x,y):

         self.menu.click_event(self.window,x,y)
         self.kup1.click_event(self.window,x,y)
         self.kup2.click_event(self.window,x,y)

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

        if self.CURRENT_LEVEL == 2:

            self.Camera.program.use()
            self.kup2.render()


    def _openlvl1(self):

        self.CURRENT_LEVEL = 1
        self.menu.visible = False
        self.menu.active = False
        self.kup1.active = True
        self.kup1.visible = True
        self.Camera.is_on = True

    def _openlvl2(self):

        self.CURRENT_LEVEL = 2
        self.menu.visible = False
        self.menu.active = False
        self.kup2.active = True
        self.kup2.visible = True
        self.Camera.is_on = True

    def _returntomenu(self):

        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.kup1.active = False
        self.kup1.visible = False
        self.Camera.is_on = False

    def _returntomenu2(self):

        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.kup2.active = False
        self.kup2.visible = False
        self.Camera.is_on = False

    
