from pyglet import gl, text, font

font.add_file('resources/def_font.ttf')

class Text:

    def __init__(self,batch):

        self._batch = batch
        self._Order = []
        self._Queue = 0
        self.add_text(0,' ',1,0,0,(0,0,0,0),1)

    def next_text(self):

        self._make_unvisible(self._Queue)
        self._Queue += 1
        self._make_visible(self._Queue)

    def add_text(self,order,Text,punto,x,y,colorRGBA,width):

        label = text.Label(' ',font_name='Comic Sans MS', font_size=punto,x=x,y=y,anchor_x='left',anchor_y='top',
                                color=colorRGBA,width=width, batch=self._batch, multiline=True,)

        self._Order.insert(order,[label,Text])

    def _make_visible(self,line):

        try:
            self._Order[line][0].text = self._Order[line][1]
    
        except IndexError:

            self._Queue = 0

    def _make_unvisible(self,line):

        self._Order[line][0].text = ' '
