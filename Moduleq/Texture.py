import pyglet
from pyglet.gl import *

class TextureGroup(pyglet.graphics.Group):
    def __init__(self, texture, shaderprogram):
        super().__init__()
        self.texture = texture
        self.program = shaderprogram

    def set_state(self):
        self.program.use()
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture.id)

    def unset_state(self):
        self.program.stop()
