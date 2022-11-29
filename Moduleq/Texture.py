from pyglet.image import *
from pyglet.gl import *
import ctypes
from Moduleq.ModelViewProjection import ModelView, Projection

class Texturer:
    '''Texture sınıfı'''

    def __init__(self,path):

        '''Verilen Resmi OpenGL texture'una dönüştürür
        '''


        pic = load(path)
        data = pic.get_data("RGBA", pic.width * 4)
        self.ID = GLuint(0)

        glBindTexture(GL_TEXTURE_2D, self.ID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, pic.width, pic.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)

        self.unbind()

        del pic
        del data

    def bind(self):

        '''Texture'u bağlar'''
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.ID)

    def unbind(self):

        glBindTexture(GL_TEXTURE_2D, 0)

    def kill(self):

        glDeleteTextures(1, self.ID)

class Skybox:

    def __init__(self,path):
        

        self.ID = GLuint(0)

        glGenTextures(1, self.ID)
        glBindTexture(GL_TEXTURE_CUBE_MAP, self.ID)

        pic = []
        for p in path:
            pic.append(load(p))

        for i in range(0,6):

            data = pic[i].get_data("RGBA", pic[i].width * 4)
            glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + i, 0, GL_RGBA, pic[i].width, pic[i].height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)

        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)

        del pic
        del data

        vertices = [        -1.0,  1.0, -1.0,
                            -1.0, -1.0, -1.0,
                             1.0, -1.0, -1.0,
                             1.0, -1.0, -1.0,
                             1.0,  1.0, -1.0,
                            -1.0,  1.0, -1.0,

                            -1.0, -1.0,  1.0,
                            -1.0, -1.0, -1.0,
                            -1.0,  1.0, -1.0,
                            -1.0,  1.0, -1.0,
                            -1.0,  1.0,  1.0,
                            -1.0, -1.0,  1.0,

                             1.0, -1.0, -1.0,
                             1.0, -1.0,  1.0,
                             1.0,  1.0,  1.0,
                             1.0,  1.0,  1.0,
                             1.0,  1.0, -1.0,
                             1.0, -1.0, -1.0,

                            -1.0, -1.0,  1.0,
                            -1.0,  1.0,  1.0,
                             1.0,  1.0,  1.0,
                             1.0,  1.0,  1.0,
                             1.0, -1.0,  1.0,
                            -1.0, -1.0,  1.0,

                            -1.0,  1.0, -1.0,
                             1.0,  1.0, -1.0,
                             1.0,  1.0,  1.0,
                             1.0,  1.0,  1.0,
                            -1.0,  1.0,  1.0,
                            -1.0,  1.0, -1.0,

                            -1.0, -1.0, -1.0,
                            -1.0, -1.0,  1.0,
                             1.0, -1.0, -1.0,
                             1.0, -1.0, -1.0,
                            -1.0, -1.0,  1.0,
                             1.0, -1.0,  1.0]

        self.vao = GLuint(0)
        self.vbo = GLuint(0)

        glGenVertexArrays(1, self.vao)
        glBindVertexArray(self.vao)

        glGenBuffers(1, self.vbo)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, len(vertices)*4, (GLfloat * len(vertices))(*vertices) , GL_STATIC_DRAW)
        glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,12, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glBindVertexArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindTexture(GL_TEXTURE_CUBE_MAP, 0)

        del vertices


    def bind(self):

        glBindVertexArray(self.vao)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_CUBE_MAP, self.ID)

    def unbind(self):

        glBindVertexArray(0)

    def draw(self):

        glDepthFunc(GL_LEQUAL)
        self.bind()
        glDrawArrays(GL_TRIANGLES, 0, 36)
        self.unbind()
        glDepthFunc(GL_LESS)
        
    def kill(self):

        glDeleteVertexArrays(1, self.vao)
        glDeleteBuffers(1, self.vbo)
        glDeleteTextures(1, self.ID)