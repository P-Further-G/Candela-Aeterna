from pyglet.gl import *
import ctypes

class Shader:
    '''OpenGL shader programı oluşturur.
    '''

    #TODO: will have its own uniforms.

    def __init__(self,vertexsourcepath,fragmentsourcepath):

        '''__init__() komutu.
Vertex Shader ve Fragment Shader yolu alır.
        '''

        vertexsource = bytes(open(vertexsourcepath,"r").read(),'utf-8')
        fragmentsource = bytes(open(fragmentsourcepath,"r").read(),'utf-8')


        vertex_buff= ctypes.create_string_buffer(vertexsource)
        c_vertex= ctypes.cast(ctypes.pointer(ctypes.pointer(vertex_buff)), ctypes.POINTER(ctypes.POINTER(GLchar)))
        vertex_shader= glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertex_shader, 1, c_vertex, None)
        glCompileShader(vertex_shader)


        fragment_buff= ctypes.create_string_buffer(fragmentsource)
        c_fragment= ctypes.cast(ctypes.pointer(ctypes.pointer(fragment_buff)), ctypes.POINTER(ctypes.POINTER(GLchar)))
        fragment_shader= glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment_shader, 1, c_fragment, None)
        glCompileShader(fragment_shader)

        self.shader= glCreateProgram()
        glAttachShader(self.shader, vertex_shader)
        glAttachShader(self.shader, fragment_shader)
        glLinkProgram(self.shader)

        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

        del vertexsource
        del fragmentsource
        del vertex_buff
        del c_vertex
        del fragment_buff
        del c_fragment


    def use(self,pm,mvm):
        '''Shaderı bağlar.'''

        glUseProgram(self.shader)
        pm.Send()
        mvm.Send()

    def getlocation(self,uniform):
        '''Shader'dan bir uniformun konumunu verir.'''
        converted = uniform.encode('utf-8')
        return glGetUniformLocation(self.shader, ctypes.c_char_p(converted))

    def close(self):
        '''Shaderı kapatır. (0. Shadera bağlar)'''

        glUseProgram(0)

    def kill(self):

        glDeleteProgram(self.shader)
       
