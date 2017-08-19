# ONCVPSP
Optimized Norm-Conserving Vanderbilt Pseudopotential (ONCVPSP) for Quantum Espresso in UPF 
format. 

# What is ONCVPSP?
Although ultrasoft pseudopotential (USPP) and PAW pseudopotential are more powerful pseudopotentials for plane-wave DFT calculatons, norm-conserving pseudopotentials (NCPP) are still important for many advanced calculatons, such as Wannier functions or GW calculatons.   

Optimized Norm-Conserving Vanderbilt Pseudopotential (ONCVPSP) is an accurate and 
inexpansive NCPP:  
https://journals.aps.org/prb/abstract/10.1103/PhysRevB.88.085117   
Currnetly there are two major ONCVPSP database, one is provided by ABINIT's official 
website:  
http://www.abinit.org/downloads/pseudodojo/pseudodojo  
The other one is provided by sg15 database:  
http://www.quantum-simulation.org/potentials/sg15_oncv/

The former is in psp8 format which is not compatible with Quantum Espresso (QE). The later is already in UPF format but these ONCVPSP do not contain the PSWFC section (wave functions in PSP) which is required by projwfc.x, the code in QE to calculate PDOS and fatband, to project. As a result, both database are not fully compatible with QE. You will always need to regenerat your own ONCVPSP in most QE calculatons. 

# What are contained in this repository?
In this repository, I used the input data in ABINIT and Sg15 database to regenerate ONCVPSP in Quantum Espresso compatible UPF format. All ONCVPSP contains PSWFC section, so they should be compatible with all calculatons. Scalar relativistic and fully relativistic PP are both generated. If you're doing a spin-orbit calculatons, you should use fully relativistic ones. 

# Which database is more recommended?
Both database are well-tested (check their websites for benchmarks). However I would more recommend to try ABINIT's database first. Not for any special reason, just because I had less difficulty (ghost states?) in their regeneration. Some elements in scalar relativistic using sg15's inputs failed. I guess ONCVPSP v3.x code has a major revision on its scalar relativistic algorithm. Although those inputs work well in v2.x, they fail in v3.x. If you find your calculatons do not behave well for some elements (usually the heavier ones) when using abinit's ONCVPSP, use sg15 instead for those elements could solve the issues. 

# Notice
* Regeneration of scalar relativistic NCPP for Pt was't succesful for both inputs. However, you can easily find an alternative one in QE's database:    
http://www.quantum-espresso.org/pseudo-search-results/?el_id=78&unp_id=7&fun_id=12&colum_k=10&origin_id

* Naming convention:  
  xx.in => the input file for ONCVPSP generation  
  xx_ONCV_PBE_sr.upf => scalar relativistic (for non-spin-orbit calculations) 
  xx_ONCV_PBE_fr.upf => fully relativistic (for spin-orbit calculatons)

* While it is not required under the terms of the GNU GPL, it is suggested that you cite D. R. Hamann, Phys. Rev. B 88, 085117 (2013) in any publication using these pseudopotentials.
 
* Use at your own risk! You should always double check your results carefully when using pseudopotentials for materials calculatons.