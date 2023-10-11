from EPiCA.pc_ccf import pc
from EPiCA.ccf import CCF_ESPRESSO
import astropy
from astropy.io import fits
import numpy as np
import sys
import os
from EPiCA.data_loader import data_loader_main,data_load_fits

def main(path_ref,path_data,path_to_save):
    '''
    Process which run over all files and calculate RV
    Parameters
    ----------
    path_ref: string
        Path to the reference CCF
    path_data: string
        Path to the data
    path_to_save: string
        Path to the save file
    '''
    result=[]
    CCF_reference,CCF_second=data_loader_main(path_ref,path_data)
    
    if (type(CCF_second)==list):
        for i in range(0,len(CCF_second)):
            CCF_second_item=data_load_fits(CCF_second[i])
            if (set(CCF_reference.velocity)!=set(CCF_second_item.velocity)):
                print("ERROR, velocity grids are not identical")
                sys.exit(1)
            result.append(pc(CCF_reference.intensity,CCF_second_item.intensity,CCF_reference.velocity))
    else:
        if (set(CCF_reference.velocity)!=set(CCF_second.velocity)):
            print("ERROR, velocity grids are not identical")
            sys.exit(1)
    np.savez(path_to_save, result)
        
def read_path(data_file):
        paths=open(data_file,'r').read().split('\n')
        path_ref=paths[0]
        path_data=paths[1]
        path_to_save=paths[2]
        main(path_ref,path_data,path_to_save)

