from pyglet import gl, text, font

font.add_file('resources/def_font.ttf')


class Text:
    def __init__(self,metin,punto,x,y,colorRGBA,width):

        self.t = 0
        self.metin = metin
        self.label = text.Label(metin[0],font_name='UKIJ Ruqi', font_size=punto,x=x,y=y,anchor_x='left',anchor_y='top',
                                color=colorRGBA, width=width, multiline=True)

    def timed_draw(self,time,dt,win):

        self.t += dt
        leng = time/len(self.metin)
        self.draw(win)

        if self.t//leng > len(self.metin):
            return

        self.label.text = self.metin[0:int(self.t//leng)]

    def draw(self,window):

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPushMatrix()
        gl.glLoadIdentity()

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glPushMatrix()
        gl.glLoadIdentity()
        gl.glOrtho(0, window.width, 0, window.height, -1, 1)

        self.label.draw()

        gl.glPopMatrix()

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPopMatrix()