import pyglet
from Moduleq.Scene import Scene
from Moduleq.Camera import Camera
from Moduleq.Texture import TextureGroup, bgroup, Beam_Group

etiket1 = pyglet.image.load('resources/Etiket1_Simülasyonlar.png')
etiket2 = pyglet.image.load('resources/Etiket2_Ayarlar.png')
etiket3 = pyglet.image.load('resources/Etiket3_Çıkış.png')
etiket4 = pyglet.image.load('resources/Etiket4_AnaMenü.png')
başlık  = pyglet.image.load('resources/CandelaAeterna.png')
play    = pyglet.image.load('resources/menü.png')
slider1 = pyglet.image.load("resources/slider1.png")
slider2 = pyglet.image.load("resources/slider2.png")

class Level():

    def __init__(self,win):

        self.CURRENT_LEVEL = 0
        self.Camera = Camera('Shaders/VertexShader.shader','Shaders/FragmentShader.shader')
        self.Lightning = Camera('Shaders/LightVertex.shader','Shaders/LightFragment.shader')
        self.window = win
        self.time = 0

    #=============================================================>

    #=>
        self.menu = Scene(self.Camera)
        self.menu.active = True
        self.menu.visible = True

        self.menu_texture = pyglet.image.load("resources/texture.jpg").get_texture()
        self.ortam2_texture = pyglet.image.load("resources/texture.png").get_texture()


        self.grup1 = TextureGroup(self.menu_texture,self.Camera)
        self.grup2 = TextureGroup(self.ortam2_texture,self.Camera)
        self.lightgroup = Beam_Group(self.Lightning,win)


        self.Reflect = Scene(self.Lightning)
        self.Reflect.add_beam("a0",self.lightgroup,(0,    5,    0,   0,   5,  -4))
        self.Reflect.add_beam("a1",self.lightgroup,(0,    5,   -4,   0,   5,  -8))


        self.menu.add_obj_converted("lab","Models_converted/SonLab.txt",self.grup1,offset=(15,0,25))

        self.menu0 = Scene(self.Camera)
        self.menu0.active = True
        self.menu0.visible = True

        self.menu0.add_sprite("başlık",başlık,0.025,0.675,0.255,0.925)
        self.menu0.add_button('tuttifurti',etiket1,0.025,0.475,0.155,0.625,self._move_to_board)
        self.menu0.add_button('tuttifurti2',etiket2,0.025,0.275,0.155,0.425,self._openlvl2)
        self.menu0.add_button('tuttifurti3',etiket3,0.025,0.075,0.155,0.225,self._exit)

        self.menu1 = Scene(self.Camera)

        self.menu1.add_button("1goesto1",play,0.4,0.2,0.55,0.3,self._openlvl1)
        self.menu1.add_button("2goesto1",play,0.4,0.35,0.55,0.45,self._openlvl1)
        self.menu1.add_button("3goesto1",play,0.4,0.5,0.55,0.6,self._openlvl1)
        self.menu1.add_button("4goesto1",play,0.4,0.65,0.55,0.75,self._openlvl1)
        self.menu1.add_button("5goesto1",play,0.4,0.8,0.55,0.9,self._openlvl1)
        self.menu1.add_button("1goesto2",play,0.6,0.2,0.75,0.3,self._openlvl1)
        self.menu1.add_button("2goesto2",play,0.6,0.35,0.75,0.45,self._openlvl1)
        self.menu1.add_button("3goesto2",play,0.6,0.5,0.75,0.6,self._openlvl1)
        self.menu1.add_button("4goesto2",play,0.6,0.65,0.75,0.75,self._openlvl1)
        self.menu1.add_button("5goesto2",play,0.6,0.8,0.75,0.9,self._openlvl1)


        self.kup1 = Scene(self.Camera)
        self.kup1.add_obj_converted("heyo","Models_converted/Torch.txt",self.grup1,offset=(0,5,5))
        self.kup1.add_button('huuh',etiket4,0.025,0.775,0.155,0.925,self._returntomenu)
        self.kup1.add_slider("sürükleme",slider2,slider1,0.7,0.9,0.9,0.93,90)


        self.kup2 = Scene(self.Camera)
        self.kup2.add_obj_converted("hey","Models_converted/Torch.txt",self.grup1,offset=(0,0,5))
        self.kup2.add_button('huuh',etiket4,0.025,0.775,0.155,0.925,self._returntomenu2)
        self.kup2.add_slider("sürükleme",slider2,slider1,0.5,0.9,0.7,0.93,90,value=45)
        

    #=============================================================>


    def resize(self,width,height):

        self.Camera.projection = pyglet.math.Mat4.perspective_projection(width/float(height),z_near=0.1, z_far=255,fov=50.0)
        self.Camera.program['projection'] = self.Camera.projection

        self.Lightning.projection = pyglet.math.Mat4.perspective_projection(width/float(height),z_near=0.1, z_far=255,fov=50.0)
        self.Lightning.program['projection'] = self.Lightning.projection

    def scale(self,width,height):

        self.menu.scale_acc_to_window(width,height)
        self.menu0.scale_acc_to_window(width,height)
        self.menu1.scale_acc_to_window(width,height)
        self.kup1.scale_acc_to_window(width,height)
        self.kup2.scale_acc_to_window(width,height)

    def on_click(self,x,y):

        self.menu.click_event(self.window,x,y)
        self.menu0.click_event(self.window,x,y)
        self.menu1.click_event(self.window,x,y)
        self.kup1.click_event(self.window,x,y)
        self.kup2.click_event(self.window,x,y)

    def on_release(self):

        self.kup1.release_event()

    def on_scroll(self,scroll_y):

        if self.Camera.is_on:
            self.Camera.will_move_to(self.Camera.pos_x, 
                                     self.Camera.pos_y,
                                     self.Camera.pos_z + 2*scroll_y)


        if self.Lightning.is_on:
            self.Lightning.will_move_to(self.Lightning.pos_x, 
                                     self.Lightning.pos_y,
                                     self.Lightning.pos_z + 2*scroll_y)

    def on_drag(self,x,y,dx,dy):

        can_rotate = self.kup1.drag_event(self.window,x,y)

        if can_rotate:
            if self.Camera.is_on:
                self.Camera.will_rotate_to(self.Camera.angle_x + dy/20, self.Camera.angle_y + -dx/20)

            if self.Lightning.is_on:
                self.Lightning.will_rotate_to(self.Lightning.angle_x + dy/20, self.Lightning.angle_y + -dx/20)


    def on_update(self,dt):

        self.time += dt
        self.Camera.Smooth_Translate(5*dt)
        self.Camera.Smooth_Rotate(3*dt)

        self.Reflect.rotate_beam("a1",(self.kup1.sliders["sürükleme"]['value'] - self.kup1.sliders["sürükleme"]['multiplier']/2)*2 ,1,'x')

        self.Lightning.Smooth_Translate(5*dt)
        self.Lightning.Smooth_Rotate(3*dt)

        if self.CURRENT_LEVEL == 0: self.Camera.will_rotate_to(self.Camera.angle_x, self.Camera.angle_dy + 0.25*dt)

        if self.Lightning.is_on: self.Lightning.program['utime'] = self.time

    #=============================================================>

    def show(self):

        if self.CURRENT_LEVEL == 0: 

            self.menu.render()
            self.menu0.render()

        if self.CURRENT_LEVEL == 0.5:

            self.menu.render()
            self.menu1.render()

        if self.CURRENT_LEVEL == 1:

            self.menu.render()
            self.kup1.render()
            self.Reflect.render()

        if self.CURRENT_LEVEL == 2:

            self.Reflect.render()
            self.kup2.render()


    def _openlvl1(self):

        self.Camera.RTZ()
        self.Lightning.RTZ()
        self.CURRENT_LEVEL = 1

        self.menu1.visible = False
        self.menu1.active = False

        self.kup1.active = True
        self.kup1.visible = True
        self.menu.visible = True
        self.menu.active = True
        self.Reflect.active = True
        self.Reflect.visible = True

        self.Lightning.is_on = True
        self.Camera.is_on = True


    def _openlvl2(self):

        self.Camera.RTZ()
        self.Lightning.RTZ()
        self.CURRENT_LEVEL = 2
        self.menu.visible = False
        self.menu.active = False
        self.kup2.active = True
        self.kup2.visible = True
        self.Camera.is_on = True

        self.Reflect.active = True
        self.Reflect.visible = True
        self.Lightning.is_on = True


    def _returntomenu(self):

        self.Camera.MenuSettings()
        self.Lightning.MenuSettings()
        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.menu0.visible = True
        self.menu0.active = True

        self.kup1.active = False
        self.kup1.visible = False
        self.Reflect.active = False
        self.Reflect.visible = False

        self.Lightning.is_on = False
        self.Camera.is_on = False

    def _returntomenu2(self):

        self.Camera.MenuSettings()
        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.kup2.active = False
        self.kup2.visible = False
        self.Camera.is_on = False

        self.Reflect.active = False
        self.Reflect.visible = False
        self.Lightning.is_on = False

    def _exit(self):

        pyglet.app.exit()

    def _move_to_board(self):

        self.CURRENT_LEVEL = 0.5
        self.Camera.will_rotate_to(0,0)
        self.Camera.will_move_to(-4,-10,8)

        self.Camera.is_on = False
        self.Lightning.is_on = False

        pyglet.clock.schedule_once(self._open_menu1,2.25)

    def _open_menu1(self,dt):
        self.menu0.active = False
        self.menu0.visible = True
        self.menu1.visible = True
        self.menu1.active = True



