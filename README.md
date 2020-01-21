# ONCVPSP
Optimized Norm-Conserving Vanderbilt Pseudopotential (ONCVPSP) for Quantum Espresso in UPF 
format. 

# What is ONCVPSP?
Although ultrasoft pseudopotential (USPP) and PAW pseudopotential are very powerful pseudopotentials for plane-wave based DFT calculatons, norm-conserving pseudopotentials (NCPP) are still important for many advanced calculatons such as Wannier functions or GW calculatons.   

Optimized Norm-Conserving Vanderbilt Pseudopotential (ONCVPSP) is an accurate and 
inexpansive NCPP:  
https://journals.aps.org/prb/abstract/10.1103/PhysRevB.88.085117   
Currnetly there are two major ONCVPSP database, one is provided by ABINIT's official 
website:  
http://www.abinit.org/downloads/pseudodojo/pseudodojo  
The other one is provided by sg15 database:  
http://www.quantum-simulation.org/potentials/sg15_oncv/

The former is in psp8 format which is not compatible with Quantum Espresso (QE). The later is already in UPF format but these ONCVPSPs do not contain the PSWFC section (wave functions in PSP) which is required by projwfc.x, the code in QE to calculate PDOS and fatband, to project. As a result, neither of them is fully compatible with QE and, more importantly, neither one provide fully-relativisitc version (needed for spin-orbit coupling). 

In short, you will always need to regenerate your own ONCVPSP in most QE calculatons especially when it comes to spin-orbit coupling. That's why I create the project. 

# What are contained in this repository?
In this repository, I extract the input data from ABINIT and Sg15 database to regenerate ONCVPSP in Quantum Espresso compatible UPF format. All ONCVPSP contains PSWFC section, so they should be compatible with all calculatons. Scalar relativistic and fully relativistic PP are both generated. If you're doing a spin-orbit calculatons, you should use fully relativistic ones. 

# Which database is more recommended?
Both database are well-tested (check their websites for benchmarks). However I would more recommend to try ABINIT's database first. Not for any special reason, just because I had less difficulty (ghost states?) in their regeneration. Some elements in scalar relativistic using sg15's inputs failed. I guess ONCVPSP v3.x code has a major revision on its scalar relativistic algorithm. Although those inputs work well in v2.x, they fail in v3.x. If you find your calculatons do not behave well for some elements (usually the heavier ones) when using abinit's ONCVPSP, use sg15 instead for those elements could solve the issues. 

# Others
* Naming convention:  
  xx.in => the input file for ONCVPSP generation  
  xx_ONCV_PBE_sr.upf => scalar relativistic (for non-spin-orbit calculations)   
  xx_ONCV_PBE_fr.upf => fully relativistic (for spin-orbit calculatons)

* While it is not required under the terms of the GNU GPL, it is suggested that you cite D. R. Hamann, Phys. Rev. B 88, 085117 (2013) in any publication using these pseudopotentials.
 
* Use at your own risk! Although I used exactly the same input parameters as in the original ABINIT and SG15 database to regenerate ONCVPSPs in UPF format, the ONCVPSP code I used was v3.x where the original ABINIT and SG15 database were generate by v2.x. Therefore, the calculated results could be different. You should always double check your results carefully.
