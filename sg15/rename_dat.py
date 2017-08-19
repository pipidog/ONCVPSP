import os
wkdir='/media/sf_Work/sg15/dat/'

os.chdir(wkdir)
flist=os.listdir(wkdir)
for fname in flist:
  atname=fname.replace('_',' ').split()[0]
  if len(atname)<=2:
    os.system('mv '+fname+' '+atname+'.in')
