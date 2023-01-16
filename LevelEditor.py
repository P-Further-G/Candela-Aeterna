import pyglet
from Moduleq.Scene import Scene
from Moduleq.Camera import Camera
from Moduleq.Texture import TextureGroup, bgroup

foto = pyglet.image.load('resources/menü.png')

class Level():

    def __init__(self,win):

        self.CURRENT_LEVEL = 0
        self.Camera = Camera('Shaders/VertexShader.shader','Shaders/FragmentShader.shader')
        self.Black_cam = Camera('Shaders/plainvertex.shader','Shaders/plainshader.shader')
        self.window = win

    #=============================================================>

    #=>
        self.menu = Scene(self.Camera)
        self.menu.active = True
        self.menu.visible = True
        self.menu.set_texture("resources/Kup.png")
        self.grup1 = TextureGroup(self.menu.texture,self.Camera)
        self.grup2 = bgroup(self.Black_cam)

        self.menu.add_obj_converted("lab","Models_converted/Lab.txt",self.grup1)
        self.menu.add_obj_converted("lab","Models_converted/Lab.txt",self.grup2)
        self.menu.add_button('tuttifurti',foto,0.025,0.6,0.1,0.7,self._openlvl1)
        self.menu.Text.show_always("Küp",25,5,500,(160,0,0,255),500)
        self.menu.add_button('tuttifurti2',foto,0.025,0.4,0.1,0.5,self._openlvl2)
        self.menu.Text.show_always("Ortam",25,5,350,(0,0,0,255),500)
        self.menu.add_button('tuttifurti3',foto,0.025,0.2,0.1,0.3,self._openlvl3)
        self.menu.Text.show_always("Yazı",25,5,250,(0,0,0,255),500)


    #=>
        self.kup1 = Scene(self.Camera)
        self.kup1.set_texture("resources/Kup.png")
        self.grup3 = TextureGroup(self.kup1.texture,self.Camera)
        self.kup1.add_obj_converted("heyo","Models_converted/Lab.txt",self.grup3)
        self.kup1.add_obj_converted("heyo","Models_converted/Lab.txt",self.grup2)
        self.kup1.add_button('huuh',foto,0.06,0.8,0.13,0.96,self._returntomenu)

        self.kup2 = Scene(self.Camera)
        self.kup2.set_texture("resources/Kup.png")
        self.kup2.add_obj_converted("hey","Models_converted/Kure.txt",self.grup1)
        self.kup2.add_obj_converted("hey","Models_converted/Kure.txt",self.grup2)
        self.kup2.add_button('huuh',foto,0.06,0.8,0.13,0.96,self._returntomenu2)
        
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

        self.Black_cam.projection = pyglet.math.Mat4.perspective_projection(width/float(height),z_near=0.1, z_far=255,fov=50.0)
        self.Black_cam.program['projection'] = self.Black_cam.projection

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

    def on_scroll(self,scroll_y):

        if self.Camera.is_on:
            self.Camera.will_move_to(self.Camera.pos_x, 
                                     self.Camera.pos_y,
                                     self.Camera.pos_z + 2*scroll_y)

        if self.Black_cam.is_on:
            self.Black_cam.will_move_to(self.Black_cam.pos_x, 
                                     self.Black_cam.pos_y,
                                     self.Black_cam.pos_z + 2*scroll_y)

    def on_drag(self,dx,dy):

        if self.Camera.is_on:
            self.Camera.will_rotate_to(self.Camera.angle_x + dy/20, self.Camera.angle_y + -dx/20)

        if self.Black_cam.is_on:
            self.Black_cam.will_rotate_to(self.Black_cam.angle_x + dy/20, self.Black_cam.angle_y + -dx/20)

    def on_update(self,dt):

        self.Camera.Smooth_Translate(5*dt)
        self.Camera.Smooth_Rotate(3*dt)

        self.Black_cam.Smooth_Translate(5*dt)
        self.Black_cam.Smooth_Rotate(3*dt)

        if self.CURRENT_LEVEL == 0: self.Camera.will_rotate_to(self.Camera.angle_x, self.Camera.angle_dy + 0.5*dt)
        if self.CURRENT_LEVEL == 0: self.Black_cam.will_rotate_to(self.Black_cam.angle_x, self.Black_cam.angle_dy + 0.5*dt)

    #=============================================================>

    def show(self):

        if self.CURRENT_LEVEL == 0:

            self.menu.render()

        if self.CURRENT_LEVEL == 1:

            self.kup1.render()

        if self.CURRENT_LEVEL == 2:

            self.kup2.render()

        if self.CURRENT_LEVEL == 3:

            self.metin.render()


    def _openlvl1(self):

        self.Camera.RTZ()
        self.Black_cam.RTZ()
        self.CURRENT_LEVEL = 1
        self.menu.visible = False
        self.menu.active = False
        self.kup1.active = True
        self.kup1.visible = True
        self.Camera.is_on = True
        self.Black_cam.is_on = True

    def _openlvl2(self):

        self.Camera.RTZ()
        self.Black_cam.RTZ()
        self.CURRENT_LEVEL = 2
        self.menu.visible = False
        self.menu.active = False
        self.kup2.active = True
        self.kup2.visible = True
        self.Camera.is_on = True
        self.Black_cam.is_on = True

    def _openlvl3(self):

        self.Camera.RTZ()
        self.Black_cam.RTZ()
        self.CURRENT_LEVEL = 3
        self.menu.visible = False
        self.menu.active = False
        self.metin.active = True
        self.metin.visible = True
        self.Camera.is_on = False
        self.Black_cam.is_on = False


    def _returntomenu(self):

        self.Camera.MenuSettings()
        self.Black_cam.MenuSettings()
        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.kup1.active = False
        self.kup1.visible = False
        self.Camera.is_on = False
        self.Black_cam.is_on = False

    def _returntomenu2(self):

        self.Camera.MenuSettings()
        self.Black_cam.MenuSettings()
        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.kup2.active = False
        self.kup2.visible = False
        self.Camera.is_on = False
        self.Black_cam.is_on = False

    def _returntomenu3(self):

        self.Camera.MenuSettings()
        self.Black_cam.MenuSettings()
        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.metin.active = False
        self.metin.visible = False
        self.Camera.is_on = False
        self.Black_cam.is_on = False

    def _changetext(self):

        self.metin.Text.next_text()
