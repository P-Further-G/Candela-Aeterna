import pyglet
from pyglet.gl import *
import ctypes


def ShadowMap(width,height):

    shadowmapFBO = GLuint(0)
    glGenFramebuffers(1, shadowmapFBO)

    smWidth = ctypes.c_uint(width)
    smHeight = ctypes.c_uint(height)
    shadowmap = GLuint(0)
    glGenTextures(1, shadowmap)
    glBindTexture(GL_TEXTURE_2D, shadowmap)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT, smWidth, smHeight, 0, GL_DEPTH_COMPONENT, GL_FLOAT, None)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)

    glBindFrameBuffer(GL_FRAMEBUFFER, shadowmapFBO)
    glFrameBufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, shadowmap, 0)
    glDrawBuffer(GL_NONE)
    glReadBuffer(GL_NONE)
    glBindFrameBuffer(GL_FRAMEBUFFER, 0)

    return shadowmapFBO, shadowmap





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
        self.program.program.stop()

class TextureShadowGroup(pyglet.graphics.Group):
    def __init__(self):
        super().__init__()


    def set_state(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glDisable(GL_CULL_FACE)

    def unset_state(self):
        glEnable(GL_CULL_FACE)

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
        self.program.program['modelview'] = self.program.modelview @ self.program.rotx @ self.program.roty
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