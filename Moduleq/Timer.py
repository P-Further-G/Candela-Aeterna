class Time:
    '''Basit sayaç sınıfı'''
    def __init__(self):
        '''__init__() komutu.'''
        self.dt = 0
        self.tick = 0

    def count(self,dt):
        '''Kareler arası geçen zamanı alır. FPS i çıktı verir.'''
        self.dt += dt
        self.tick += 1
        if self.dt >= 1: print(self.tick); self.tick, self.dt = 0,0