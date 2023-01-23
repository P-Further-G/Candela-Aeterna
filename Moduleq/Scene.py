import pyglet
from pyglet.gl import *
from math import sin,cos,radians
from Moduleq.ObjLoader import ObjLoader
from Moduleq.Writer import Text

class Scene:
    
    def __init__(self,shader):

        self.scene_obj = {}
        self.scene_sprites = {}
        self.buttons = {}
        self.beams = {}
        self.points = {}
        self.shaderprogram = shader.program
        self.batch = pyglet.graphics.Batch()
        self.visible = False
        self.active = False
        self.Text = Text(self.batch)


    def set_texture(self,path):

        self.texture = pyglet.image.load(path).get_texture()

    def add_object(self,obj,group):

        self.scene_obj[obj['name']] = self.shaderprogram.vertex_list_indexed(int(len(obj['positions'])/3),GL_TRIANGLES, 
                                                      obj['indices'],batch=self.batch,group=group, position=('f',(obj['positions'])),
                                                      normal=('f',(obj['normals'])),
                                                      texcoord=('f',(obj['texcoords'])))
    
    def add_beam(self,name,group,xyz):

        self.beams[name] = [self.shaderprogram.vertex_list(2,GL_LINES,batch=self.batch,group=group,position=('f',xyz), type=('b',(1,1))), xyz]
        self.points[name] = self.shaderprogram.vertex_list(2,GL_POINTS,batch=self.batch,group=group,position=('f',xyz), type=('b',(0,0)))

    def _change_beam(self,name,xyz):

        self.beams[name][0].set_attribute_data("position", xyz)
        self.points[name].set_attribute_data("position", xyz)

    def rotate_beam(self,name,degree,anchor):

        xyz = self.beams[name][1]
        d = -radians(degree)

        if anchor == 1:
            x = xyz[3] - xyz[0]
            y = xyz[4] - xyz[1]
            x2 = x*cos(d) - y*sin(d) + xyz[0]
            y2 = x*sin(d) + y*cos(d) + xyz[1]
            data = (xyz[0],xyz[1],xyz[2],x2,y2,xyz[5])

        if anchor == 2:
            x = xyz[0] - xyz[3]
            y = xyz[1] - xyz[4]
            x2 = x*cos(d) - y*sin(d)
            y2 = x*sin(d) + y*cos(d)
            data = (xyz[0],x2,y2,xyz[3],xyz[4],xyz[5])

        self._change_beam(name,data)



    def add_obj_file(self,name,path,group):

        vertices, indices, normals, texture = ObjLoader(path)
        obj = self.getobj(name, vertices, indices, normals, texture)
        self.add_object(obj,group)

    def add_obj_converted(self,name,path,group):
        with open(path,"r") as file:
            data = file.readlines()
            obj = self.getobj(name, list(map(float,data[0].split(' '))), list(map(int,data[1].split(' '))), list(map(float,data[2].split(' '))), list(map(float,data[3].split(' '))))
            self.add_object(obj,group)

    def add_sprite(self,name:str,image, x1:float, y1:float, x2:float, y2:float, z=1.0):

        self.scene_sprites[name] = {'sprite_data':pyglet.sprite.Sprite(img=image, x=x1, y=y1, z=z, batch = self.batch),
                                    'width':image.width,
                                    'height':image.height,
                                    'pos_x1':x1,
                                    'pos_x2':x2-x1,
                                    'pos_y1':y1,
                                    'pos_y2':y2-y1}

    def add_button(self,name,image,x1:float,y1:float,x2:float,y2:float,todo):

        self.buttons[name] = {'pos_x1':x1,
                              'pos_x2':x2,
                              'pos_y1':y1,
                              'pos_y2':y2,
                              'func':todo}

        self.add_sprite(name,image,x1,y1,x2,y2)


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

        if self.visible: 
            
            self.batch.draw()


    @staticmethod
    def getobj(name:str, poz:list, ind:list, normals:list, texcoord:list):

        return {'name':name, 'positions':poz, 'indices':ind, 'normals':normals, 'texcoords':texcoord}