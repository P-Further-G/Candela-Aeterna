from pyglet import gl, text, font

font.add_file('resources/def_font.ttf')


class Text:
    def __init__(self,metin,punto,x,y,colorRGBA,width,batch):

        self.t = 0
        self.swrite = False
        self.metin = metin
        self.label = text.Label(' ',font_name='UKIJ Ruqi', font_size=punto,x=x,y=y,anchor_x='left',anchor_y='top',
                                color=colorRGBA,width=width, batch=batch, multiline=True)

    def timed_draw(self,time,dt):

        if self.swrite:

            self.t += dt
            leng = time/len(self.metin)

            if self.t//leng > len(self.metin):
                return

            self.label.text = self.metin[0:int(self.t//leng)]

        else:

            self.t = 0
            self.label.text = ' '

    def draw(self):

        if self.swrite:

            self.label.text = self.metin
