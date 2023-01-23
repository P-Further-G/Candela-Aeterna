import pyglet
from pyglet.gl import *

class TextureGroup(pyglet.graphics.Group):
    def __init__(self, texture, shaderprogram):
        super().__init__()
        self.texture = texture.id
        self.program = shaderprogram

    def set_state(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.program.program.use()
        self.program.program['projection'] = self.program.projection
        self.program.program['modelview'] = self.program.modelview @ self.program.rotx @ self.program.roty
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)

    def unset_state(self):
        pass

class bgroup(pyglet.graphics.Group):

    def __init__(self, shader):
        super().__init__()

        self.program = shader


    def set_state(self):

        self.program.program.use()
        self.program.program['projection'] = self.program.projection
        self.program.program['modelview'] = self.program.modelview @ self.program.rotx @ self.program.roty

    def unset_state(self):

        pass


class Beam_Group(pyglet.graphics.Group):

    def __init__(self, shader, win):
        super().__init__()

        self.program = shader
        self.win = win

    def set_state(self):

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.program.program.use()
        self.program.program['projection'] = self.program.projection
        self.program.program['modelview'] = self.program.modelview @ self.program.rotx @ self.program.roty
        self.program.program['u_viewport'] = self.win.get_framebuffer_size()

    def unset_state(self):

        pass