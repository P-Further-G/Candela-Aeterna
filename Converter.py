import time

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


    return vertices, indices, normals, texcoords


path = str(input("Path =>"))
name = str(input("What will be its name =>"))

t1 = time.perf_counter()
vertices, indices, normals, texcoords = ObjLoader(path)

with open(f"Models_converted/{name}.txt".format(name = name),"w") as file:

    file.write(' '.join(map(str,vertices))+"\n")
    file.write(' '.join(map(str,indices))+"\n")
    file.write(' '.join(map(str,normals))+"\n")
    file.write(' '.join(map(str,texcoords))+"\n")
    t2 = time.perf_counter()
    t = t2-t1
    print("Finished in "+str(t)+" seconds")

x = input("press any key to close")
