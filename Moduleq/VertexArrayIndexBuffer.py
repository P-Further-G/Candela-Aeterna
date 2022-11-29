from pyglet.gl import *
import ctypes

class Obje:
    '''Obje sınıfı.'''

    def __init__(self,positions,indices,texture,normals):
        '''Bir Buffer oluşturur.
        Vertex bilgileri (pozisyonlar,texture koordinantları, normaller)
        ve Sıralama (indices) alır.
        '''
        self.positions = positions
        self.normals = normals
        self.indices = indices
        self.textures = texture

        #VBO ve IB oluşturur
        self.vbo = GLuint(0)
        self.ib = GLuint(0)

        #VBO data--->
        glGenBuffers(1, self.vbo)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, (len(positions)+len(normals)+len(texture))*4, None, GL_STATIC_DRAW)

        #Datayı parça parça koy
        glBufferSubData(GL_ARRAY_BUFFER, 0, len(positions)*4, (GLfloat * len(positions))(*positions))
        glBufferSubData(GL_ARRAY_BUFFER, len(positions)*4, len(normals)*4, (GLfloat * len(normals))(*normals))
        glBufferSubData(GL_ARRAY_BUFFER, (len(positions)+len(normals))*4, len(texture)*4, (GLfloat * len(texture))(*texture))

        #Location =
        # ? ayarlaması
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(len(positions)*4))
        glEnableVertexAttribArray(1)

        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8, ctypes.c_void_p((len(positions)+len(normals))*4))
        glEnableVertexAttribArray(2)

        #IB data--->
        glGenBuffers(1, self.ib)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ib)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(indices)* 4, (GLuint * len(indices))(*indices) ,GL_STATIC_DRAW)

        self.unbind()

    def bind(self):
        '''Objeyi Bağlar'''

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ib)

    def unbind(self):

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def draw(self):
        '''Objeyi Çizer'''

        self.bind()
        glDrawElements(GL_TRIANGLES,len(self.indices),GL_UNSIGNED_INT,0)
        self.unbind()

    def kill(self):

        glDeleteBuffers(1, self.vbo)
        glDeleteBuffers(1, self.ib)
