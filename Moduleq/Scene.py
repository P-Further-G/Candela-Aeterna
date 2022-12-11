from pyglet.gl import *

class Scene:
    
    def __init__(self,shader):

        self.scene = {}
        self.shaderprogram = shader.program

        
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

        data = self.shaderprogram.vertex_list_indexed(int(len(obj['positions'])/3), GL_TRIANGLES, 
                                                      obj['indices'], position=('f',(obj['positions'])),
                                                      normal=('f',(obj['normals'])),
                                                      texcoord=('f',(obj['texcoords'])))

        self.scene[obj['name']] = data

    def render(self, *exclude):

        for name,obj in self.scene.items():

            if not name in exclude:

                obj.draw(GL_TRIANGLES)


    @staticmethod
    def getobj(name:str, poz:list, ind:list, normals:list, texcoord:list):

        dic = {'name':name, 'positions':poz, 'indices':ind, 'normals':normals, 'texcoords':texcoord}
        return dic