import trimesh
import numpy
import sys


filename = sys.argv[1]
faces = numpy.loadtxt(filename+'.face', dtype=int, skiprows=3, usecols=(0,1,2))
vertices = numpy.loadtxt(filename+'.vert', dtype=float, skiprows=3, usecols=(0,1,2))
mesh = trimesh.Trimesh(vertices = vertices, faces= faces-1)
mesh_split = mesh.split()
print("Found %i meshes"%len(mesh_split))
for mesh_i in mesh_split:
    print (len(mesh_i.faces))
vertices_split = mesh_split[0].vertices
faces_split = mesh_split[0].faces
print("Mesh 1: %i elements"%len(faces_split))
vertices_split = mesh_split[0].vertices
faces_split = mesh_split[0].faces
numpy.savetxt(filename+'_split.face', faces_split+1, fmt='%i')
numpy.savetxt(filename+'_split.vert', vertices_split, fmt='%1.5f')
