class ObjLoader:

    '''.obj Formatindaki dosyaları listeler.'''

    def __init__(self,path):

        '''Dosyanın "yol"unu alır.
        '''

        vlist = []
        tlist = []
        nlist = []
        sayac = []
        isayac = 0

        self.vertices = []
        self.texcoords = []
        self.normals = []
        self.indices = []

        dosya = open(path,"r")
        for ver in dosya:

            v = ver.split(" ")

            if v[0] == 'v':

                vlist.append([float(v[1]),float(v[2]),float(v[3])])

            elif v[0] == 'vt':

                tlist.append([float(v[1]),float(v[2])])

            elif v[0] == 'vn':

                nlist.append([float(v[1]),float(v[2]),float(v[3])])

            if v[0] == 'f':
                
                face = v[1].split("/")
                face[0] = int(face[0])-1
                face[1] = int(face[1])-1
                face[2] = int(face[2])-1

                data = (face[0],face[1],face[2])

                if not data in sayac:

                    sayac.append(data)

                    self.indices.append(isayac)
                    isayac += 1

                    self.vertices.append(vlist[face[0]][0])
                    self.vertices.append(vlist[face[0]][1])
                    self.vertices.append(vlist[face[0]][2])

                    self.texcoords.append(tlist[face[1]][0])
                    self.texcoords.append(tlist[face[1]][1])

                    self.normals.append(nlist[face[2]][0])
                    self.normals.append(nlist[face[2]][1])
                    self.normals.append(nlist[face[2]][2])

                else:

                    self.indices.append(sayac.index(data))


                face = v[2].split("/")
                face[0] = int(face[0])-1
                face[1] = int(face[1])-1
                face[2] = int(face[2])-1

                data = (face[0],face[1],face[2])

                if not data in sayac:

                    sayac.append(data)

                    self.indices.append(isayac)
                    isayac += 1

                    self.vertices.append(vlist[face[0]][0])
                    self.vertices.append(vlist[face[0]][1])
                    self.vertices.append(vlist[face[0]][2])

                    self.texcoords.append(tlist[face[1]][0])
                    self.texcoords.append(tlist[face[1]][1])

                    self.normals.append(nlist[face[2]][0])
                    self.normals.append(nlist[face[2]][1])
                    self.normals.append(nlist[face[2]][2])

                else:

                    self.indices.append(sayac.index(data))


                face = v[3].split("/")
                face[0] = int(face[0])-1
                face[1] = int(face[1])-1
                face[2] = int(face[2])-1

                data = (face[0],face[1],face[2])

                if not data in sayac:

                    sayac.append(data)

                    self.indices.append(isayac)
                    isayac += 1

                    self.vertices.append(vlist[face[0]][0])
                    self.vertices.append(vlist[face[0]][1])
                    self.vertices.append(vlist[face[0]][2])

                    self.texcoords.append(tlist[face[1]][0])
                    self.texcoords.append(tlist[face[1]][1])

                    self.normals.append(nlist[face[2]][0])
                    self.normals.append(nlist[face[2]][1])
                    self.normals.append(nlist[face[2]][2])

                else:

                    self.indices.append(sayac.index(data))



        dosya.close()
        del dosya
        del vlist
        del tlist
        del nlist
        del sayac
        del isayac

