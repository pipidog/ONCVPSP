# This code is to generate the ONCVPSP using the psp8 PSP provided
# by Abinit. 
import os, sys

class oncvpsp_upf:
    def __init__(self,wkdir):
        if (wkdir[-1]!='/') & (wkdir[-1]!='\\'):
            wkdir=wkdir+'/'    

        self.wkdir=wkdir
        self.ex_code={'PZ':3,'PBE':4, 'PW91':-109134, 'PBESOL':-116133,\
        'REVPBE':-102130,'BP':-106132,'BLYP':-106131,'WC':-118130}

    def __grep__(self,txtlines,kws,reg=False):
        # search for line numbers from a textlines where contains the keywords
        if reg:
            ln=[ n for n,txt in enumerate(txtlines) if (re.search(kws,txt)!=None)]
        else:
            ln=[ n for n,txt in enumerate(txtlines) if (txt.find(kws)!=-1)]
            
        return ln
        
    def psp8extract(self,atname):
        with open(self.wkdir+atname+'.psp8','r') as file:
            flines=file.readlines()
        inpdat=flines[self.__grep__(flines,'# ATOM')[0]:self.__grep__(flines,'</INPUT>')[0]]
        
        with open(atname+'.in','w') as file:
            file.writelines(inpdat)
            
            
    def input_gen(self,atname,ex_type):

        # read abinit psp8 file
        with open(self.wkdir+atname+'.in','r') as file:
            flines=file.readlines()
        atdat=flines[2].split()


        atdat[-1]='upf'
        atdat[-2]=str(self.ex_code[ex_type])
        
        flines[2]='{0[0]}   {0[1]}   {0[2]}   {0[3]}   {0[4]}   {0[5]}\n'.format(atdat)
        print(flines[2])
        with open(self.wkdir+atname+'.in','w') as file:
            file.writelines(flines)

    def oncv_gen(self,oncv_root,atname,wf_type):
        if (oncv_root[-1]!='/') & (oncv_root[-1]!='\\'):
            oncv_root=oncv_root+'/'
        # check ex_type
        with open(self.wkdir+atname+'.in','r') as file:
            flines=file.readlines()
        ex_type=[]
        for ex in list(self.ex_code.keys()):
            if self.ex_code[ex]==float(flines[2].split()[-2]):
                ex_type=ex
                break
                
        if ex_type==[]:
            print('Error: ex_type not defined in '+atname+'.in')
            sys.exit()
            
        # generate oncvpsp
        inpname=atname+'.in'
        outname=atname+'_ONCV_'+ex_type+'_'+wf_type+'.upf'
        if wf_type=='fr':
            os.system(oncv_root+'src/oncvpspr.x <'+self.wkdir+inpname+' > '+self.wkdir+outname)
        elif wf_type=='sr':
            os.system(oncv_root+'src/oncvpsp.x <'+self.wkdir+inpname+' > '+self.wkdir+outname)
        elif wf_type=='nr':
            os.system(oncv_root+'src/oncvpspnr.x <'+self.wkdir+inpname+' > '+self.wkdir+outname)
        
        # delete information part
        with open(self.wkdir+outname,'r') as file:
            flines=file.readlines()
        
        lstart=self.__grep__(flines,'Begin PSP_UPF')
        lend=self.__grep__(flines,'END_PSP')
        if (lstart==[]) | (lend==[]):
            print('Error: '+outname+' failed!')
            os.system('mv '+self.wkdir+outname+' '+self.wkdir+outname[0:-3]+'fail')
        else:
            with open(self.wkdir+outname,'w') as file:
                file.writelines(flines[lstart[0]+1:lend[0]])

# test =================================================================
if __name__=='__main__':
    # parameter
    wkdir='/media/sf_Work/sg15/dat'
    oncv_root='/home/pipidog/Programs/oncvpsp-3.3.0'
    task='upf'  #'psp2in', 'sg2in', 'upf'   
    ex_type='PBE'
    wf_type='sr' # 'nr','sr', 'fr'
    # Main -----------------
    psp=oncvpsp_upf(wkdir)
    flist=os.listdir(wkdir)
    if task=='psp2upf':    
        for f in flist:
            if f.find('.psp8')!=-1:
                atname=f.replace('.',' ').split()[0]
                print('generating atom = '+atname)
                psp.psp8extract(atname)          
                psp.input_gen(atname,ex_type)
                psp.oncv_gen(oncv_root,atname,ex_type,wf_type)
                
    elif task=='upf':
        for f in flist:
            atname=(f.replace('_',' ').split()[0]).replace('.',' ').split()[0]
            if f.find(atname+'.in')!=-1:
                print(' =================')
                print(' ')
                print('generating atom = '+atname+', ex_type='+ex_type+', wf_type='+wf_type)        
                psp.input_gen(atname,ex_type)
                psp.oncv_gen(oncv_root,atname,wf_type)
