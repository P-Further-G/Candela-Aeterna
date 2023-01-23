import pyglet
from Moduleq.Scene import Scene
from Moduleq.Camera import Camera
from Moduleq.Texture import TextureGroup, bgroup, Beam_Group

foto = pyglet.image.load('resources/menü.png')
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

        self.menu_texture = pyglet.image.load("resources/Kup.png").get_texture()
        self.ortam2_texture = pyglet.image.load("resources/texture.png").get_texture()


        self.grup1 = TextureGroup(self.menu_texture,self.Camera)
        self.grup2 = TextureGroup(self.ortam2_texture,self.Camera)
        self.lightgroup = Beam_Group(self.Lightning,win)


        self.Reflect = Scene(self.Lightning)
        self.Reflect.add_beam("a0",self.lightgroup,(0,    0,   2,   0,  0,  -20))
        self.Reflect.add_beam("a1",self.lightgroup,(0,    0,  -20,   0,  0,  -40))


        self.menu.add_obj_converted("lab","Models_converted/Lab.txt",self.grup1)
        self.menu.add_button('tuttifurti',foto,0.025,0.6,0.1,0.7,self._openlvl1)
        self.menu.Text.show_always("Küp",25,5,500,(160,0,0,255),500)
        self.menu.add_button('tuttifurti2',foto,0.025,0.4,0.1,0.5,self._openlvl2)
        self.menu.Text.show_always("Ortam",25,5,350,(0,0,0,255),500)
        self.menu.add_button('tuttifurti3',foto,0.025,0.2,0.1,0.3,self._openlvl3)
        self.menu.Text.show_always("Yazı",25,5,250,(0,0,0,255),500)
        self.menu.add_button('tuttifurti4',foto,0.025,0.05,0.1,0.18,self._openlvl4)


        self.kup1 = Scene(self.Camera)
        self.kup1.add_obj_converted("heyo","Models_converted/Lab.txt",self.grup1)
        self.kup1.add_button('huuh',foto,0.06,0.8,0.13,0.96,self._returntomenu)


        self.kup2 = Scene(self.Camera)
        self.kup2.add_obj_converted("hey","Models_converted/Torch.txt",self.grup1,offset=(0,0,5))
        self.kup2.add_button('huuh',foto,0.06,0.8,0.13,0.96,self._returntomenu2)
        self.kup2.add_slider("sürükleme",slider2,slider1,0.5,0.9,0.7,0.93,90,value=45)
        

        self.metin = Scene(self.Camera)
        self.metin.add_button('gerigeri',foto,0.06,0.8,0.13,0.96,self._returntomenu3)
        self.metin.add_button('gerivegeri',foto,0.22,0.42,0.33,0.57,self._changetext)
        cümle = """MERHABA bügün sizinle minecraft videosu çekicez elmas bulucaz maden kazıcaz vs. vs. like atıp abone olmayı unutmayın paylaşın yorum yapın şimdi video 10 dakika olsun diye outro koyucam beğenmeye devam edin tşk tşk tşk öd np"""
        self.metin.Text.add_text(1,cümle,16,500,400,(150,70,0,255),500)
        self.metin.Text.add_text(2,"aaaaA",22,500,400,(150,70,0,50),500)


    #=============================================================>


    def resize(self,width,height):

        self.Camera.projection = pyglet.math.Mat4.perspective_projection(width/float(height),z_near=0.1, z_far=255,fov=50.0)
        self.Camera.program['projection'] = self.Camera.projection

        self.Lightning.projection = pyglet.math.Mat4.perspective_projection(width/float(height),z_near=0.1, z_far=255,fov=50.0)
        self.Lightning.program['projection'] = self.Lightning.projection

    def scale(self,width,height):

        self.menu.scale_acc_to_window(width,height)
        self.kup1.scale_acc_to_window(width,height)
        self.kup2.scale_acc_to_window(width,height)
        self.metin.scale_acc_to_window(width,height)

    def on_click(self,x,y):

        self.menu.click_event(self.window,x,y)
        self.kup1.click_event(self.window,x,y)
        self.kup2.click_event(self.window,x,y)
        self.metin.click_event(self.window,x,y)

    def on_release(self):

        self.kup2.release_event()

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

        can_rotate = self.kup2.drag_event(self.window,x,y)

        if can_rotate:
            if self.Camera.is_on:
                self.Camera.will_rotate_to(self.Camera.angle_x + dy/20, self.Camera.angle_y + -dx/20)

            if self.Lightning.is_on:
                self.Lightning.will_rotate_to(self.Lightning.angle_x + dy/20, self.Lightning.angle_y + -dx/20)


    def on_update(self,dt):

        self.time += dt
        self.Camera.Smooth_Translate(5*dt)
        self.Camera.Smooth_Rotate(3*dt)

        self.Reflect.rotate_beam("a1",(self.kup2.sliders["sürükleme"]['value'] - self.kup2.sliders["sürükleme"]['multiplier']/2)*2 ,1,'x')

        self.Lightning.Smooth_Translate(5*dt)
        self.Lightning.Smooth_Rotate(3*dt)

        if self.CURRENT_LEVEL == 0: self.Camera.will_rotate_to(self.Camera.angle_x, self.Camera.angle_dy + 0.5*dt)

        if self.Lightning.is_on:

            self.Lightning.program['utime'] = self.time

    #=============================================================>

    def show(self):

        if self.CURRENT_LEVEL == 0:

            self.menu.render()

        if self.CURRENT_LEVEL == 1:

            self.kup1.render()

        if self.CURRENT_LEVEL == 2:

            self.Reflect.render()
            self.kup2.render()

        if self.CURRENT_LEVEL == 3:

            self.metin.render()

        if self.CURRENT_LEVEL == 4:

            self.Reflect.render()


    def _openlvl1(self):

        self.Camera.MenuSettings()
        self.CURRENT_LEVEL = 1
        self.menu.visible = False
        self.menu.active = False
        self.kup1.active = True
        self.kup1.visible = True
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

    def _openlvl3(self):

        self.Camera.RTZ()
        self.CURRENT_LEVEL = 3
        self.menu.visible = False
        self.menu.active = False
        self.metin.active = True
        self.metin.visible = True
        self.Camera.is_on = False


    def _openlvl4(self):

        self.Camera.RTZ()
        self.Lightning.RTZ()
        self.CURRENT_LEVEL = 4
        self.menu.visible = False
        self.menu.active = False
        self.Reflect.active = True
        self.Reflect.visible = True
        self.Camera.is_on = False
        self.Lightning.is_on = True

    def _returntomenu(self):

        self.Camera.MenuSettings()
        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.kup1.active = False
        self.kup1.visible = False
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

    def _returntomenu3(self):

        self.Camera.MenuSettings()
        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.metin.active = False
        self.metin.visible = False
        self.Camera.is_on = False

    def _returntomenu4(self):

        self.Camera.MenuSettings()
        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.Reflect.active = False
        self.Reflect.visible = False
        self.Camera.is_on = False
        self.Lightning.is_on = False

    def _changetext(self):

        self.metin.Text.next_text()
