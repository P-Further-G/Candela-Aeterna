import pyglet
from pyglet.gl import *


class Scene:
    
    def __init__(self,shader):

        self.scene_obj = {}
        self.scene_sprites = {}
        self.buttons = {}
        self.shaderprogram = shader.program
        self.batch = pyglet.graphics.Batch()
        self.visible = False
        self.active = False

        poz =  [
        -1,-1,-1,
        -1, 1,-1,
         1,-1,-1,
         1, 1,-1,
        -1,-1, 1,
        -1, 1, 1,
         1,-1, 1,
         1, 1, 1 
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

        default_obj = self.getobj('def',poz,ind,normals,tex)
        self.add_object(default_obj)


    def add_object(self,obj):

        self.scene_obj[obj['name']] = self.shaderprogram.vertex_list_indexed(int(len(obj['positions'])/3),GL_TRIANGLES, 
                                                      obj['indices'],batch=self.batch, position=('f',(obj['positions'])),
                                                      normal=('f',(obj['normals'])),
                                                      texcoord=('f',(obj['texcoords'])))

    def add_sprite(self,name:str,image, x1:float, y1:float, x2:float, y2:float, z=-1.0):

        self.scene_sprites[name] = {'sprite_data':pyglet.sprite.Sprite(img=image, x=x1, y=y1, z=z, batch = self.batch),
                                    'width':image.width,
                                    'height':image.height,
                                    'pos_x1':x1,
                                    'pos_x2':x2-x1,
                                    'pos_y1':y1,
                                    'pos_y2':y2-y1}

    def add_button(self,name,x1:float,y1:float,x2:float,y2:float,todo):

        self.buttons[name] = {'pos_x1':x1,
                              'pos_x2':x2,
                              'pos_y1':y1,
                              'pos_y2':y2,
                              'func':todo}


    def scale_acc_to_window(self,width,height):

        for sprite in self.scene_sprites.values():
            sprite['sprite_data'].x = width*sprite['pos_x1']
            sprite['sprite_data'].y = height*sprite['pos_y1']
            sprite['sprite_data'].scale_x = width/sprite['width']*sprite['pos_x2']
            sprite['sprite_data'].scale_y = height/sprite['height']*sprite['pos_y2']


    def click_event(self,win,x,y):

        for button in self.buttons.values():

            if self.active and button['pos_x1']*win.width <= x <= button['pos_x2']*win.width and button['pos_y1']*win.height <= y <= button['pos_y2']*win.height:

                button['func']()

    def flip_visiblity(self):

        self.visible = not self.visible

    def delete_obj(self,name):

        self.scene_obj[name].delete()

    def render(self):

        if self.visible: self.batch.draw()


    @staticmethod
    def getobj(name:str, poz:list, ind:list, normals:list, texcoord:list):

        return {'name':name, 'positions':poz, 'indices':ind, 'normals':normals, 'texcoords':texcoord}