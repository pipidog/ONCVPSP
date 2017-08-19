# ONCVPSP
Optimized Norm-Conserving Vanderbilt Pseudopotential (ONCVPSP) for Quantum Espresso in UPF 
format. 

# What is ONCVPSP?
Although ultrasoft pseudopotential (USPP) and PAW pseudopotential are more recommend
pseudopotentials for plane-wave DFT calculatons, norm-conserving pseudopotentials (NCPP)
are still important for many advanced calculatons, such as Wannier functions or GW
calculatons. 

Optimized Norm-Conserving Vanderbilt Pseudopotential (ONCVPSP) is an accurate and 
inexpansive NCPP. Currnetly there are two major ONCVPSP database, one is provided
by ABINIT's official website:
http://www.abinit.org/downloads/pseudodojo/pseudodojo
The other one is provided by sg15 database:
http://www.quantum-simulation.org/potentials/sg15_oncv/

The former is in psp8 format which is not compatible with Quantum Espresso (QE). The later
is already in UPF format but these ONCVPSP do not contain the <PSWFC> section which 
is required by projwfc.x (the code in QE to calculate PDOS and fatband). As a result, 
both database are not completely compatible for QE. You will always need to regenerat
your own ONCVPSP in most QE calculatons. 

# What are contained in this repository?
In this repository, I used the input data in ABINIT and Sg15 database to regenerat
ONCVPSP in Quantum Espresso compatible UPF format. All ONCVPSP contains <PWSCF> section, 
so should be compatible will all calculatons. Scalar relativistic and fully relativistic
PP are both generated. If you're doing a spin-orbit calculatons, please use fully
relativistic ones. 

# Which one is more recommended?
Both database are well-tested and reliable. However I would more recommend the ONCVPSP 
generated based on ABINIT's database! Not for any special reason, just because I had less 
difficulty (ghost state?) when generating them (I guess ONCVPSP v2.x would work better 
than v3.x for sg15 inputs?). If you find your calculatons do not behave well for some 
atoms, use sg15 instead for those atoms could solve the issues. 

* scalar relativistic NCPP for Pt was not generated successfully neither ABINIT's input 
nor sg15's input. However, you can easily find one in QE's database:
http://www.quantum-espresso.org/pseudo-search-results/?el_id=78&unp_id=7&fun_id=12&colum_k=10&origin_id

* Naming convention:
xx.in => the input file for PSP generation
xx_ONCV_PBE_sr.upf => scalar relativistic
xx_ONCV_PBE_fr.upf => fully relativistic (for spin-orbit calculatons)
