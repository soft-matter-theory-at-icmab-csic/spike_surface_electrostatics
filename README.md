This repository contains the following files necessary to run PyGBe calculations of the electrostatic interactions between the spike protein (WT, Delta and Omicron variants) and a negatively charged surface with a density charge of -1e*/nm^2:


- pqr_spike_protein folder: It contains the pqr files for the 6 configurations per variant used in the paper.

- surface.pqr: Pqr file of the planar surface. Note that the spacing does not match the typical pqr file. However, the file is properly read by the PyGBe software.

- config_file.config: Configuration file used for the calculation with PyGBe.

- parameters.param: Parameter file used in the PyGBe calculations.

- change_salt_concentration: PyGBe configuration files corresponfing to different Kappa.

- General_method_example: Example of pqr file of the Auxiliary I system (protein and planar surface with no charge) and Auxiliary II system (protein with no charge and charged planar surface). Note that the spacing does not match the typical pqr file. However, the file is properly read by the PyGBe software. 
