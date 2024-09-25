# Interaction of the SARS-CoV-2 Spike protein (WT, Delta and Omicron variants) with charged surfaces
## Description
This repository contains the following files necessary to run [PyGBe](https://github.com/pygbe/pygbe) calculations of the electrostatic interactions between the spike protein (WT, Delta and Omicron variants) and a charged surface corresponding to our preprint [ChemRxiv. 2024](https://chemrxiv.org/engage/chemrxiv/article-details/66f19a2acec5d6c142f9dbe7).


- pqr_spike_protein folder: It contains the pqr files for the 6 configurations per variant used in the paper.

- surface.pqr: Pqr file of the planar surface. Note that the spacing does not match the typical pqr file. The file will only be read correctly by the PyGBe software, not by other visualisation programs.

- surface files: Necessary input files to generate the surface files of the protein and planar surface. 
  
- config_file.config: Configuration file used for the calculation with PyGBe.

- parameters.param: Parameter file used in the PyGBe calculations.

- Free Energy method: Example of pqr files for the Free Energy calculations reported in Section 3.1 of our paper. We provide example pqr files for the Auxiliary I system (protein and planar surface with no charge) and Auxiliary II system (protein with no charge and charged planar surface) and reference system. Note that the data format does not match exactly the standard pqr file format but the pqr format used by PyGBe. The files will only be read correctly by the PyGBe software, not by other visualisation programs.
  
- change_salt_concentration: PyGBe configuration files corresponding to the calculations reported in the paper (section 3.2) using different Kappa values (i.e. different salt concentrations of 15 mM, 50 mM, 150 mM and 1500mM). The same configuration files were used for the three different variants and distances of separation.

## PyGBe scheme
![alt text](https://github.com/soft-matter-theory-at-icmab-csic/spike_surface_electrostatics/blob/main/pygbe.drawio_white.png?raw=true)


## Citation

Please cite our work corresponding to this dataset as follows:
Domingo M, Guzman H, Kanduc M, Faraudo J. *Electrostatic interaction between SARS-CoV-2 and charged surfaces: Spike protein evolution changed the game.* [ChemRxiv. 2024](https://chemrxiv.org/engage/chemrxiv/article-details/66f19a2acec5d6c142f9dbe7) ; doi:10.26434/chemrxiv-2024-mrmjk This content is a preprint and has not been peer-reviewed.
