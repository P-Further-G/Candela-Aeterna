from pyglet.graphics.shader import Shader, ShaderProgram
from pyglet.math import Mat4
from math import sin,cos,radians

class Camera:


    def __init__(self,vertexsourcepath,fragmentsourcepath):

        vert_source=open(vertexsourcepath,"r").read()
        frag_source=open(fragmentsourcepath,"r").read()

        vert_Shader = Shader(vert_source, 'vertex')
        frag_Shader = Shader(frag_source, 'fragment')
        self.program = ShaderProgram(vert_Shader, frag_Shader)

        self.projection= Mat4.perspective_projection(1280/float(620),z_near=0.1, z_far=255,fov=60.0)
        self.modelview = Mat4([ 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, -15.0, 1.0])
        self.program['projection'] = self.projection
        self.program['modelview'] = self.modelview

        self.rotx = Mat4([ 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0])
        self.roty = Mat4([ 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0])

        self.pos_x = 0.0
        self.pos_y = 0.0
        self.pos_z = -15.0

        self.dx = 0.0
        self.dy = 0.0
        self.dz = -15.0

        self.angle_x = 0
        self.angle_y = 0

        self.angle_dx = 0
        self.angle_dy = 0



        self.is_on = False

        del vert_source
        del frag_source

    def Rotate(self,dx,dy):

        if not -1 <= self.angle_x + dx <= 1: 
            
            self.angle_dx = self.angle_x

        else:

            self.angle_x += dx


        self.angle_y += dy

        self.rotx= Mat4([1,0,0,0,0,cos(self.angle_x),-sin(self.angle_x),0,0,sin(self.angle_x),cos(self.angle_x),0,0,0,0,1])

        self.roty= Mat4([cos(self.angle_y),0,sin(self.angle_y),0,0,1,0,0,-sin(self.angle_y),0,cos(self.angle_y),0,0,0,0,1])

        self.program['modelview'] =  self.roty @ self.rotx @ self.modelview 


    def Translate(self, tx, ty, tz):

        self.pos_x += tx
        self.pos_y += ty
        self.pos_z += tz

        self.modelview = Mat4([ *self.modelview[0:12], self.pos_x, self.pos_y, self.pos_z, 1])
        self.program['modelview'] = self.roty @ self.rotx @ self.modelview

    def will_move_to(self,dx,dy,dz):

        self.dx = dx
        self.dy = dy
        self.dz = dz

    def Smooth_Translate(self,smoothness):

        tx, ty, tz = self.dx - self.pos_x, self.dy - self.pos_y, self.dz - self.pos_z
        self.Translate(tx*smoothness,ty*smoothness,tz*smoothness)

    def will_rotate_to(self,dx,dy):

        self.angle_dx = dx
        self.angle_dy = dy

    def Smooth_Rotate(self,smoothness):

        dx, dy = self.angle_dx - self.angle_x, self.angle_dy - self.angle_y
        self.Rotate(dx*smoothness,dy*smoothness)