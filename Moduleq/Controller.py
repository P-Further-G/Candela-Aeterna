from pyglet import window
from math import sin, cos, pi

class Controller:


    '''Klavye girişlerinin ne yapacağını belirleyen sınıf.
    '''

    def __init__(self,keys,Speed,RotationSpeed):


        '''__init__ () komutu.
pyglet.window.key.KeyStateHandler() Alır.
Normal Hızı Alır.
Dönüş Hızını Alır.
        '''


        self.keys = keys
        self.speed = Speed
        self.rotspeed = RotationSpeed



    def Control(self,mwm,rot,dt):


        '''Klavye girişlerinin ne yapacağını belirler.
Değiştirmek için kaynağı düzenleyin.
ModelViewMatrix ve iki kare arası geçen zamanı alır.
        '''

        
        #W Tuşu ==>
        if self.keys[window.key.W]:

            mwm.Translate(sin(mwm.dy)*dt*self.speed,0, cos(mwm.dy)*dt*self.speed)
        
        #S Tuşu ==>
        if self.keys[window.key.S]:

            mwm.Translate(sin(mwm.dy)*dt*-self.speed, 0, cos(mwm.dy)*dt*-self.speed)
        
        #A Tuşu ==>
        if self.keys[window.key.A]:

            mwm.Translate(sin(mwm.dy + pi/2)*dt*self.speed,0,cos(mwm.dy + pi/2)*dt*self.speed)
        
        #D Tuşu ==>
        if self.keys[window.key.D]:

            mwm.Translate(sin(mwm.dy + pi/2)*dt*-self.speed,0,cos(mwm.dy + pi/2)*dt*-self.speed)

        #SPACE tuşu ==>
        if self.keys[window.key.SPACE]:

            mwm.Translate(0,-dt*self.speed,0)

        #SHIFT tuşu ==>
        if self.keys[window.key.LSHIFT]:

            mwm.Translate(0,dt*self.speed,0)


        self.Rotate(mwm,rot[0],rot[1])
        rot[0] = 0
        rot[1] = 0




    def Rotate(self,mwm,dx,dy):
        '''Farenin değişimine göre ekranı döndürür.
x Konumunun değişimi alır.
y Konumunun değişimi alır.
        '''

        mwm.rotateY(-dx* self.rotspeed )
        mwm.rotateX(dy *self.rotspeed )
