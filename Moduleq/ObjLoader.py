import sys 

def ObjLoader(path):

    vlist = []
    tlist = []
    nlist = []
    sayac = []
    isayac = 0

    vertices = []
    texcoords = []
    normals = []
    indices = []

    with open(path) as dosya:
        for ver in dosya:

            v = ver.split(" ")

            if v[0] == 'v':

                vlist.append((float(v[1]),float(v[2]),float(v[3])))

            elif v[0] == 'vt':

                tlist.append((float(v[1]),float(v[2])))

            elif v[0] == 'vn':

                nlist.append((float(v[1]),float(v[2]),float(v[3])))

            if v[0] == 'f':

                face = v[1].split("/")
                face[0] = int(face[0])-1
                face[1] = int(face[1])-1
                face[2] = int(face[2])-1

                data = (face[0],face[1],face[2])

                if not data in sayac:

                    sayac.append(data)

                    indices.append(isayac)
                    isayac += 1

                    vertices.append(vlist[face[0]][0])
                    vertices.append(vlist[face[0]][1])
                    vertices.append(vlist[face[0]][2])

                    texcoords.append(tlist[face[1]][0])
                    texcoords.append(tlist[face[1]][1])

                    normals.append(nlist[face[2]][0])
                    normals.append(nlist[face[2]][1])
                    normals.append(nlist[face[2]][2])

                else:

                    indices.append(sayac.index(data))


                face = v[2].split("/")
                face[0] = int(face[0])-1
                face[1] = int(face[1])-1
                face[2] = int(face[2])-1

                data = (face[0],face[1],face[2])

                if not data in sayac:

                    sayac.append(data)

                    indices.append(isayac)
                    isayac += 1

                    vertices.append(vlist[face[0]][0])
                    vertices.append(vlist[face[0]][1])
                    vertices.append(vlist[face[0]][2])

                    texcoords.append(tlist[face[1]][0])
                    texcoords.append(tlist[face[1]][1])

                    normals.append(nlist[face[2]][0])
                    normals.append(nlist[face[2]][1])
                    normals.append(nlist[face[2]][2])

                else:

                    indices.append(sayac.index(data))


                face = v[3].split("/")
                face[0] = int(face[0])-1
                face[1] = int(face[1])-1
                face[2] = int(face[2])-1

                data = (face[0],face[1],face[2])

                if not data in sayac:

                    sayac.append(data)

                    indices.append(isayac)
                    isayac += 1

                    vertices.append(vlist[face[0]][0])
                    vertices.append(vlist[face[0]][1])
                    vertices.append(vlist[face[0]][2])

                    texcoords.append(tlist[face[1]][0])
                    texcoords.append(tlist[face[1]][1])

                    normals.append(nlist[face[2]][0])
                    normals.append(nlist[face[2]][1])
                    normals.append(nlist[face[2]][2])

                else:

                    indices.append(sayac.index(data))


    print((sys.getsizeof(tlist)+sys.getsizeof(vlist)+sys.getsizeof(nlist)+sys.getsizeof(sayac)+
           sys.getsizeof(vertices)+sys.getsizeof(indices)+sys.getsizeof(normals)+sys.getsizeof(texcoords))/1024)

    del vlist
    del tlist
    del nlist
    del sayac
    del isayac

    return vertices, indices, normals, texcoords



