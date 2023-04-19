import pyglet
from Moduleq.Scene import Scene
from Moduleq.Camera import Camera
from Moduleq.Texture import TextureGroup, TextureGlassGroup, Beam_Group, TextureShadowGroup, ShadowGroup
from Moduleq.FrameBuffer import FrameBuffer
from Moduleq.Metin import *

etiket1 = pyglet.image.load('resources/Etiket1_Simülasyonlar.png')
etiket2 = pyglet.image.load('resources/Etiket2_Ayarlar.png')
etiket3 = pyglet.image.load('resources/Etiket3_Çıkış.png')
etiket4 = pyglet.image.load('resources/Etiket4_AnaMenü.png')
başlık  = pyglet.image.load('resources/CandelaAeterna.png')
play    = pyglet.image.load('resources/aaa.png')

ikm     = pyglet.image.load('resources/İnce kenarlı mercek.png')
ikmka   = pyglet.image.load('resources/İnce kenarlı mercek ka.png')
kkm     = pyglet.image.load('resources/Kalın kenarlı mercek.png')
kkmka    = pyglet.image.load('resources/Kalın kenarlı mercek ka.png')
tvyg    = pyglet.image.load('resources/tam ve yarım gölge.png')
tvygka  = pyglet.image.load('resources/Tam ve yarım gölge ka.png')

slider1 = pyglet.image.load("resources/slider1.png")
slider2 = pyglet.image.load("resources/slider2.png")
arkaplan= pyglet.image.load("resources/arkaplan.png")

class Level():

    def __init__(self,win):

        self.CURRENT_LEVEL = 0
        self.Camera = Camera('Shaders/def_vert.shader','Shaders/def_frag.shader')
        self.Lightning = Camera('Shaders/light_vert.shader','Shaders/light_frag.shader')
        self.Shadow = Camera('Shaders/shadow_vert.shader','Shaders/shadow_frag.shader')
        self.FBOshadow = Camera('Shaders/shadowmapv.shader','Shaders/shadowmapf.shader')

        self.FBOshadow.view = pyglet.math.Mat4([ 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, -25.0, 1.0])
        self.fbo = FrameBuffer()
        self.buffers = pyglet.image.get_buffer_manager()
        self.window = win
        self.time = 0
    #=============================================================>

    #=>
        self.menu = Scene(self.Camera)
        self.menu.active = True
        self.menu.visible = True

        self.menu_texture = pyglet.image.load("resources/texture.jpg").get_texture()
        self.cam_texture = pyglet.image.load("resources/cam.png").get_texture()

        self.grup1 = TextureGroup(self.menu_texture,self.Camera)
        self.grup2 = TextureGlassGroup(self.cam_texture,self.Camera)

        self.grup3 = TextureShadowGroup(self.buffers,win,self.Shadow,self.FBOshadow,self.menu_texture)
        self.grup4 = ShadowGroup(self.buffers,win,self.FBOshadow,self.Shadow)
        

        self.lightgroup = Beam_Group(self.Lightning,win)




        self.menu.add_obj_converted("lab","Models_converted/EnSonLab.txt",self.grup1,offset=(15,-10,25))

        self.menu0 = Scene(self.Camera)
        self.menu0.active = True
        self.menu0.visible = True

        self.menu0.add_sprite("başlık",      başlık,0.025,0.675,0.37,0.925)
        self.menu0.add_button('tuttifurti', etiket1,0.025,0.450,0.200,0.635,self._move_to_board)
        self.menu0.add_button('tuttifurti2',etiket2,0.025,0.275,0.175,0.435,self._openlvl2)
        self.menu0.add_button('tuttifurti3',etiket3,0.025,0.075,0.175,0.235,self._exit)

        self.menu1 = Scene(self.Camera)

        self.menu1.add_button("1goesto1",ikm,0.4,0.65,0.6,0.85,self._openlvl1)
        self.menu1.add_button("1goesto2",kkm,0.4,0.45,0.6,0.65,self._openlvl2)
        self.menu1.add_button("1goesto3",tvyg,0.4,0.25,0.6,0.45,self._openlvl3)

        self.menu1.add_button("2goesto1",ikmka,0.65,0.65,0.85,0.85,self._openlvl1)
        self.menu1.add_button("2goesto2",kkmka,0.65,0.45,0.85,0.65,self._openlvl2)
        self.menu1.add_button("2goesto3",tvygka,0.65,0.25,0.85,0.45,self._openlvl3)

        self.kup1 = Scene(self.Camera)

        self.kup1.add_obj_converted("heyo","Models_converted/Fener.txt",self.grup1,offset=(0,-0.07,2))
        self.kup1.add_obj_converted("cam","Models_converted/ince_mercek.txt",self.grup2,offset=(0,0,0))
       

        self.kup1.add_button('huuh',etiket4,0.025,0.775,0.155,0.925,self._returntomenu)
        self.kup1.add_slider("sürükleme",slider2,slider1,0.7,0.9,0.9,0.93,10)

        self.KalınMercek = Scene(self.Camera)

        self.KalınMercek.add_obj_converted("heyo","Models_converted/Fener.txt",self.grup1,offset=(0,-0.07,2))
        self.KalınMercek.add_obj_converted("cam","Models_converted/kalın_mercek.txt",self.grup2,offset=(0,0,0))
        self.KalınMercek.add_button('huuh',etiket4,0.025,0.775,0.155,0.925,self._returntomenu2)
        self.KalınMercek.add_slider("sürükleme",slider2,slider1,0.7,0.9,0.9,0.93,10)


        self.Reflect = Scene(self.Lightning)
        self.Reflect.add_beam("a0",self.lightgroup,(0,    0,    2,   0,   0,  0))
        self.Reflect.add_beam("a1",self.lightgroup,(0,    0,    0,   0,   0,  -10))
       
        
        self.Reflect.add_beam("b0",self.lightgroup,(0,   0.15,    2,   0,  0.15,  0))
        self.Reflect.add_beam("b1",self.lightgroup,(0,   0.15,    0,   0,  0.15,  -10))
        self.Reflect.rotate_beam("b1",30,1,'x')

        self.Reflect.add_beam("c0",self.lightgroup,(0,   -0.15,    2,   0,  -0.15,  0))
        self.Reflect.add_beam("c1",self.lightgroup,(0,   -0.15,    0,   0,  -0.15,  -10))
        self.Reflect.rotate_beam("c1",-30,1,'x')

        self.konuanlatımı1 = Scene(self.Camera)
        self.konuanlatımı1.add_sprite("arka",arkaplan, 0.025,0.1,0.35,0.65,z=0)
        self.konuanlatımı1.Text.add_text(1,metin1,20,0.08,0.57,(0,0,0,255),300,self.window.width,self.window.height)
        self.konuanlatımı1.Text.add_text(2,metin2,20,0.08,0.57,(0,0,0,255),300,self.window.width,self.window.height)
        self.konuanlatımı1.Text.add_text(3,metin3,20,0.08,0.57,(0,0,0,255),300,self.window.width,self.window.height)
        self.konuanlatımı1.add_button("nexto",play,0.025,0.1,0.1,0.2,self.next_text)

        self.Gölge = Scene(self.Shadow)
        self.Shadowscene = Scene(self.FBOshadow)

        self.Gölge.add_obj_converted("perde","Models_converted/Perde.txt",self.grup3,offset=(0,-4,0))
        self.Gölge.add_obj_converted("kup","Models_converted/kagitadam.txt",self.grup3,offset=(0,0,5))

        self.Shadowscene.add_obj_converted("perde","Models_converted/Perde.txt",self.grup4,offset=(0,-4,0))
        self.Shadowscene.add_obj_converted("kup","Models_converted/kagitadam.txt",self.grup4,offset=(0,0,5))
        self.Shadowscene.visible = True


    #=============================================================>


    def resize(self,width,height):

        self.Camera.projection = pyglet.math.Mat4.perspective_projection(width/float(height),z_near=0.1, z_far=255,fov=50.0)
        self.Camera.program['projection'] = self.Camera.projection

        self.Lightning.projection = pyglet.math.Mat4.perspective_projection(width/float(height),z_near=0.1, z_far=255,fov=50.0)
        self.Lightning.program['projection'] = self.Lightning.projection

        self.Shadow.projection = pyglet.math.Mat4.perspective_projection(width/float(height),z_near=0.1, z_far=255,fov=50.0)
        self.Shadow.program['projection'] = self.Shadow.projection

    def scale(self,width,height):

        self.menu.scale_acc_to_window(width,height)
        self.menu0.scale_acc_to_window(width,height)
        self.menu1.scale_acc_to_window(width,height)
        self.kup1.scale_acc_to_window(width,height)
        self.konuanlatımı1.scale_acc_to_window(width,height)
        self.KalınMercek.scale_acc_to_window(width,height)
        self.Gölge.scale_acc_to_window(width,height)

    def on_click(self,x,y):

        self.menu.click_event(self.window,x,y)
        self.menu0.click_event(self.window,x,y)
        self.menu1.click_event(self.window,x,y)
        self.kup1.click_event(self.window,x,y)
        self.konuanlatımı1.click_event(self.window,x,y)
        self.KalınMercek.click_event(self.window,x,y)
        self.Gölge.click_event(self.window,x,y)

    def on_release(self):

        self.kup1.release_event()
        self.KalınMercek.release_event()

    def on_scroll(self,scroll_y):

        if self.Camera.is_on:
            self.Camera.will_move_to(self.Camera.pos_x, 
                                     self.Camera.pos_y,
                                     self.Camera.pos_z + 2*scroll_y)


        if self.Lightning.is_on:
            self.Lightning.will_move_to(self.Lightning.pos_x, 
                                     self.Lightning.pos_y,
                                     self.Lightning.pos_z + 2*scroll_y)

        if self.Shadow.is_on:
            self.Shadow.will_move_to(self.Shadow.pos_x, 
                                     self.Shadow.pos_y,
                                     self.Shadow.pos_z + 2*scroll_y)

    def on_drag(self,x,y,dx,dy):

        can_rotate = self.kup1.drag_event(self.window,x,y) and self.KalınMercek.drag_event(self.window,x,y)

        if can_rotate:
            if self.Camera.is_on:
                self.Camera.will_rotate_to(self.Camera.angle_x + dy/20, self.Camera.angle_y + -dx/20)

            if self.Lightning.is_on:
                self.Lightning.will_rotate_to(self.Lightning.angle_x + dy/20, self.Lightning.angle_y + -dx/20)

            if self.Shadow.is_on:
                self.Shadow.will_rotate_to(self.Shadow.angle_x + dy/20, self.Shadow.angle_y + -dx/20)


    def on_update(self,dt):

        self.time += dt
        self.Camera.Smooth_Translate(5*dt)
        self.Camera.Smooth_Rotate(3*dt)

        self.Shadow.Smooth_Translate(5*dt)
        self.Shadow.Smooth_Rotate(3*dt)


        if self.kup1.active:
            self.Reflect.rotate_beam("b1",self.kup1.sliders["sürükleme"]["value"] * self.kup1.sliders["sürükleme"]["multiplier"] ,1,'x')
            self.Reflect.rotate_beam("c1",-self.kup1.sliders["sürükleme"]["value"] * self.kup1.sliders["sürükleme"]["multiplier"],1,'x')
 
        if self.KalınMercek.active:
            self.Reflect.rotate_beam("b1",-self.KalınMercek.sliders["sürükleme"]["value"] * self.KalınMercek.sliders["sürükleme"]["multiplier"] ,1,'x')
            self.Reflect.rotate_beam("c1",self.KalınMercek.sliders["sürükleme"]["value"] * self.KalınMercek.sliders["sürükleme"]["multiplier"],1,'x')

        self.Lightning.Smooth_Translate(5*dt)
        self.Lightning.Smooth_Rotate(3*dt)

        if self.CURRENT_LEVEL == 0: self.Camera.will_rotate_to(self.Camera.angle_x, self.Camera.angle_dy - 0.25*dt)

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

            self.Reflect.render()
            self.kup1.render()
            self.konuanlatımı1.render()

        if self.CURRENT_LEVEL == 2:

            self.Reflect.render()
            self.KalınMercek.render()

        if self.CURRENT_LEVEL == 3:

            #pyglet.gl.glCullFace(pyglet.gl.GL_FRONT)

            pyglet.gl.glDisable(pyglet.gl.GL_CULL_FACE)

            pyglet.gl.glViewport(0,0,1024,1024)
            self.fbo.bind()
            self.Shadowscene.render()
            self.fbo.unbind()

            pyglet.gl.glViewport(0,0,self.window.width,self.window.height)


            pyglet.gl.glActiveTexture(pyglet.gl.GL_TEXTURE1)

            pyglet.gl.glBindTexture(pyglet.gl.GL_TEXTURE_2D, self.fbo.tex)

            pyglet.gl.glActiveTexture(pyglet.gl.GL_TEXTURE0)

            pyglet.gl.glBindTexture(self.menu_texture.target, self.menu_texture.id)

            self.Gölge.render()

            pyglet.gl.glEnable(pyglet.gl.GL_CULL_FACE)
            pyglet.gl.glCullFace(pyglet.gl.GL_BACK)

    def _openlvl1(self):

        self.Camera.RTZ()
        self.Lightning.RTZ()
        self.CURRENT_LEVEL = 1

        self.menu.visible = False
        self.menu.active = False
        self.menu1.visible = False
        self.menu1.active = False
        self.kup1.active = True
        self.kup1.visible = True
        self.Reflect.active = True
        self.Reflect.visible = True
        self.konuanlatımı1.visible = True
        self.konuanlatımı1.active = True
        self.Camera.is_on = True
        self.Lightning.is_on = True


    def _openlvl2(self):

        self.Camera.RTZ()
        self.Lightning.RTZ()
        self.CURRENT_LEVEL = 2

        self.menu.visible = False
        self.menu.active = False
        self.menu1.visible = False
        self.menu1.active = False
        self.Reflect.active = True
        self.Reflect.visible = True
        self.KalınMercek.visible = True
        self.KalınMercek.active = True
        self.Camera.is_on = True
        self.Lightning.is_on = True

    def _openlvl3(self):

        self.Camera.RTZ()
        self.Lightning.RTZ()
        self.Shadow.RTZ()
        self.FBOshadow.RTZ()
        self.CURRENT_LEVEL = 3

        self.menu.visible = False
        self.menu.active = False
        self.menu1.visible = False
        self.menu1.active = False

        self.Gölge.visible = True
        self.Gölge.active = True
        self.Shadow.is_on = True


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
        self.konuanlatımı1.visible = False
        self.konuanlatımı1.active = False

        self.Lightning.is_on = False
        self.Camera.is_on = False

    def _returntomenu2(self):

        self.Camera.MenuSettings()
        self.Lightning.MenuSettings()
        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.menu0.visible = True
        self.menu0.active = True

        self.Reflect.active = False
        self.Reflect.visible = False
        self.KalınMercek.visible = False
        self.KalınMercek.active = False

        self.Lightning.is_on = False
        self.Camera.is_on = False


    def _returntomenu3(self):

        self.Camera.MenuSettings()
        self.Lightning.MenuSettings()
        self.Shadow.MenuSettings()
        self.CURRENT_LEVEL = 0
        self.menu.visible = True
        self.menu.active = True
        self.menu0.visible = True
        self.menu0.active = True


        self.Gölge.visible = False
        self.Gölge.active = False

        self.Lightning.is_on = False
        self.Camera.is_on = False
        self.Shadow.is_on = False

    def _exit(self):

        pyglet.app.exit()

    def _move_to_board(self):

        self.CURRENT_LEVEL = 0.5
        self.Camera.will_rotate_to(0,0)
        self.Camera.will_move_to(-4,0,8,limit=False)

        self.Camera.is_on = False
        self.Lightning.is_on = False

        pyglet.clock.schedule_once(self._open_menu1,2.25)

    def _open_menu1(self,dt):
        self.menu0.active = False
        self.menu0.visible = False
        self.menu1.visible = True
        self.menu1.active = True

    def next_text(self):

        self.konuanlatımı1.Text.next_text()

