# ONCVPSP
Optimized Norm-Conserving Vanderbilt Pseudopotential (ONCVPSP) for Quantum Espresso in UPF 
format. 

These ONCVPSP are converted by the PSP8 files provided by ABINIT database: 
http://www.abinit.org/downloads/pseudodojo/pseudodojo

I used the input files of this database to regenerated ONCVPSP in Quantum Espresso compatible 
UPF format. In addition, ONCVPSP with spin-orbit coupling (fully relativistic) are also 
generated. 

Hopefully these PSPs work well. Use at your own risk. 

* scalar relativistic PSP for Pt was not generated successfully using ONCVPSP v3.3. I guess 
it will work if use v2.x. However, it is not difficult to find an altrenative scalar relativistic 
norm-conserving PSP for Pt in QE's database.

* I also generated another series of ONCVPSP based sg15 database:
http://www.quantum-simulation.org/potentials/sg15_oncv/
The original sg15 database is already in UPF format. However, the UPF files in this database
do not contain the PSWFC section. As a result, projwfc.x (fatband and PDOS calculatons) will 
not work since it requires the wave functions in the pseudopotential files for projection. Now 
the problem is fixed. If you think the abinit version ONCVPSP do not behave well for some atoms, 
you can search for altrenative ones in the sg15 folder. 