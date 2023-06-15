# Trapped_Ion_RE
Resource estimation for lattice surgery in trapped ion systems

Last updated: 15/06/23
This repository consists of:
* Quirk circuits in html format which interactively demonstrate various elements of the distillation protocol.
* Jupyter notebooks of varying degrees of importance:
      * Multiround purification.ipynb (Main working draft for simulating resource estimation)
      * Multiround success rate.ipynb (Determining how many ions are needed to collect enough entanglement over time, subjectto confidence requirments
* Mathematica notebooks: 
      * ZerrTolerance: (important) Numerical derivations for the "Ensemble Fidelity" calculations, resource estimation details for error-free circuits
      * ZYerrTolerance: Numerical deriviations for a more general mixed diagonal state. The point of this notebook is to demonstrate that we can safely treat Y errors as X errors for parity check purification.
* QST (ignore): Quantum state tomography methods for qiskit and stim -- not needed
* Old files (ignore): Self explanatory
