from pyglet.gl import *
import ctypes
from math import cos, sin, tan, radians
from copy import deepcopy

class ModelView:

    '''Basit Model Matrix sınıfı.
    '''

    def __init__(self,shader):
        '''__init__() komutu.
Model Matrix oluşturur.
Kullanılan shader'ı alır.
        '''


        self.Matrix = [ 1.0, 0.0, 0.0, 0.0,
                        0.0, 1.0, 0.0, 0.0,
                        0.0, 0.0, 1.0, 0.0,
                        0.0, 0.0, 0.0, 1.0]

        self.__new_Matrix = deepcopy( self.Matrix )

        self.x = 0
        self.y = 0
        self.z = 0

        self.dx = 0
        self.dy = 0

        self.loc = shader.getlocation("view")
        self.__poz_loc = shader.getlocation("CamPoz")
        self.__poz_Xdegree = shader.getlocation("Xdegree")
        self.__poz_Ydegree = shader.getlocation("Ydegree")



    def rotateX(self,degree):

        '''X ekseni etrafında döndürür.
Derece olarak değer alır.
        '''

    
        self.dx += radians(degree)
        self.dx = min(max(self.dx,-1.50),1.50)


    def rotateY(self,degree):


        '''Y ekseni etrafında döndürür.
Derece olarak değer alır.
        '''

        self.dy += radians(degree)

    
    def Translate(self, tx,ty,tz):


        '''3 eksende hareket ettirir.
Değişecek x-y-z değerlleri alır.
        '''

        self.x += tx
        self.y += ty
        self.z += tz

        self.Matrix[12] += tx 
        self.Matrix[13] += ty
        self.Matrix[14] += tz


    def Send(self):


        '''Her şeyi günceller.
        '''

        glUniformMatrix4fv(self.loc,1, GL_FALSE, ((ctypes.c_float * len(self.Matrix))(*self.Matrix)) )
        glUniform4f(self.__poz_loc, self.x, self.y, self.z, 0)
        glUniform1f(self.__poz_Xdegree, self.dx)
        glUniform1f(self.__poz_Ydegree, self.dy)

class Projection:


    '''Basit Projection Matrix sınıfı.
    '''



    def __init__(self, shader, aspect, zNear, zFar, fov):


        '''__init__() komutu.
Projection Matrix oluşturur.
Kullanılan shader, ekran genişliğinin yüksekliğine oranı,
En yakın mesafe, en uzak mesafe, görüş açısı alır.
        '''


        self._aspect = aspect
        self._zNear = zNear
        self._zFar = zFar
        self._fov = fov

        self.a = 1/(aspect*tan(radians(fov/2)))
        self.b = 1/(tan(radians(fov/2)))
        self.c = -(zFar+zNear)/(zFar-zNear)
        self.d = -(2*zFar*zNear)/(zFar-zNear)

        self.Matrix = [self.a,  0,  0,  0,
                       0,  self.b,  0,  0,
                       0,  0,  self.c, -1,
                       0,  0,  self.d,  0]

        self.loc = shader.getlocation("projection")


    def update(self, aspect):


        '''Ekran genişliğinin yüksekliğe oranını günceller.
        '''


        self.a = 1/(aspect*tan(radians(self._fov/2)))
        self.b = 1/(tan(radians(self._fov/2)))

        self._aspect = aspect

        self.Matrix = [self.a,  0,  0,  0,
                       0,  self.b,  0,  0,
                       0,  0,  self.c, -1,
                       0,  0,  self.d,  0]



    def Send(self):

        '''Uniform'a verileri gönderir. 
        '''

        glUniformMatrix4fv(self.loc, 1, GL_FALSE, ((ctypes.c_float * len(self.Matrix))(*self.Matrix)) )

