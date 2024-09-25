Example surface files for the protein and planar surface and input files to generate them. The surface files are necessary input of PyGBe together with the pqr file. Note that when doing the calculations at different $d_c$ both the .pqr and .vert need to be shifted in the perpendicular direction of the planar surface. 

- sensor_300x10x300_d02.face: File corresponding to the planar surface. Generated using python script https://github.com/pygbe/pygbe/blob/master/preprocessing_tools/mesh_brick.py
- sensor_300x10x300_d02.vert: File corresponding to the planar surface. Generated using python script https://github.com/pygbe/pygbe/blob/master/preprocessing_tools/mesh_brick.py
- input_protein_Mesh.prm: Nanoshaper input file necessary to generate the proteins surface ".vert" and ".face" files.
- Omicron_triangulatedSurf_split.vert.zip and Omicron_triangulatedSurf_split.face.zip: Surface files corresponding to configuration 1 of the Omicron variant at contact distance ($d_c$=2Å). Generated using Nanoshaper code https://gitlab.iit.it/SDecherchi/nanoshaper. The input parameter file specifing the characteristics of the surface is input_protein_Mesh.prm.
- Delta_triangulatedSurf_split.vert.zip and Delta_triangulatedSurf_split.face.zip: Surface files corresponding to configuration 2 of the Delta variant at contact distance ($d_c$=2Å). Generated using Nanoshaper code https://gitlab.iit.it/SDecherchi/nanoshaper. The input parameter file specifing the characteristics of the surface is input_protein_Mesh.prm.
- WT_triangulatedSurf_split.vert.zip and WT_triangulatedSurf_split.face.zip: Surface files corresponding to configuration 1 of the WT variant at contact distance ($d_c$=2Å). Generated using Nanoshaper code https://gitlab.iit.it/SDecherchi/nanoshaper. The input parameter file specifing the characteristics of the surface is input_protein_Mesh.prm.
- meshMaker.py: Trimesh python code to remove small triangulations.

