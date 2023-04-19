import pyglet
from pyglet.gl import *
import ctypes


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
        self.program.program['model'] = self.program.model @ self.program.rotx @ self.program.roty
        self.program.program['view'] = self.program.view

        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)

    def unset_state(self):
        self.program.program.stop()


class ShadowGroup(pyglet.graphics.Group):
    def __init__(self, fbo, win, shaderprogram, model):
        super().__init__()
        self.win = win
        self.program = shaderprogram
        self.fbo = fbo
        self.model = model

    def set_state(self):

        self.program.program.use()
        self.program.program['projection'] = self.program.projection
        self.program.program['depth_matrix'] = self.model.model
        self.program.program['view'] = self.program.view

    def unset_state(self):

        self.program.program.stop()

class TextureShadowGroup(pyglet.graphics.Group):
    def __init__(self, fbo, win, shaderprogram, view ,texture):
        super().__init__()
        self.fbo = fbo
        self.win = win
        self.program = shaderprogram
        self.texture = texture.id
        self.lightview = view

    def set_state(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.program.program.use()
        self.program.program['projection'] = self.program.projection
        self.program.program['model'] = self.program.model @ self.program.rotx @ self.program.roty
        self.program.program['view'] = self.program.view
        
        self.program.program['lightview'] = self.lightview.view

        self.program.program['oTexture'] = 0
        self.program.program['shadowmap'] = 1



    def unset_state(self):
        self.program.program.stop()


class TextureGlassGroup(pyglet.graphics.Group):
    def __init__(self, texture, shaderprogram):
        super().__init__()
        self.texture = texture.id
        self.program = shaderprogram

    def set_state(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.program.program.use()
        self.program.program['projection'] = self.program.projection
        self.program.program['model'] = self.program.model @ self.program.rotx @ self.program.roty
        self.program.program['view'] = self.program.view
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)

    def unset_state(self):
        self.program.program.stop()

class bgroup(pyglet.graphics.Group):

    def __init__(self, shader):
        super().__init__()

        self.program = shader


    def set_state(self):

        self.program.program.use()
        self.program.program['projection'] = self.program.projection
        self.program.program['model'] = self.program.model @ self.program.rotx @ self.program.roty
        self.program.program['view'] = self.program.view

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
        self.program.program['model'] = self.program.model @ self.program.rotx @ self.program.roty
        self.program.program['view'] = self.program.view
        self.program.program['u_viewport'] = self.win.get_framebuffer_size()

    def unset_state(self):

        pass