from pyglet.graphics.shader import Shader, ShaderProgram
from pyglet.math import Mat4

class Shaderq:


    def __init__(self,vertexsourcepath,fragmentsourcepath,pm,mwm):

        vert_source=open(vertexsourcepath,"r").read()
        frag_source=open(fragmentsourcepath,"r").read()

        vert_Shader = Shader(vert_source, 'vertex')
        frag_Shader = Shader(frag_source, 'fragment')
        self.program = ShaderProgram(vert_Shader, frag_Shader)
        self.pm = pm
        self.mwm = mwm
        self.program['projection'] = pm
        self.program['modelview'] = mwm
        self.program.attributes.update()


        """
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
        """

        del vert_source
        del frag_source

        #del vertex_buff
        #del c_vertex
        #del fragment_buff
        #del c_fragment

