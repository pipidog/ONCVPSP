# ONCVPSP
Optimized Norm-Conserving Vanderbilt Pseudopotential (ONCVPSP) for Quantum Espresso in UPF 
format. 

These ONCVPSP are converted by the PSP8 files provided by ABINIT database: 
http://www.abinit.org/downloads/pseudodojo/pseudodojo

I used the input files of this database to generated ONCVPSP in Quantum Espresso compatible 
UPF format. In addition, ONCVPSP with spin-orbit coupling (fully relativistic) are also 
generated. 

Hopefully these PSPs work well. Use at your own risk. 

* scalar relativistic PSP for Pt was not generated successfully using ONCVPSP v3.3. I guess 
it will work if use v2.x. However, it is not difficult to find an altrenative scalar relativistic 
norm-conserving PSP for Pt in QE's database.
