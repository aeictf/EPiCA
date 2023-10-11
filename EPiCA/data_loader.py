import sys
import os
from EPiCA.ccf import CCF_ESPRESSO
import astropy
from astropy.io import fits
import numpy as np

def data_load_fits(path):
    '''
    Loading of a fits file.
    Current version works only for the one CCF from 2D array.
    Parameters
    ----------
    path: string
        Path to the file
    '''
    hdul=fits.open(path)
    velocity_grid=np.arange(hdul[0].header['HIERARCH ESO RV START'],hdul[0].header['HIERARCH ESO RV START']+hdul[0].header['HIERARCH ESO RV STEP']*hdul[1].header['NAXIS1'],hdul[0].header['HIERARCH ESO RV STEP'])
    CCF=CCF_ESPRESSO(hdul[1].data[170],velocity_grid)
    return CCF
            
def data_load_txt_of_files(path):
    '''
    Loading of a text file containing several paths.
    Parameters
    ----------
    path: string
        Path to the file
    '''
    open_file=open(path,'r')
    CCF_second=open_file.read().split("\n")
    open_file.close()
    return CCF_second
            
def data_loader_main(path_to_reference,path_to_data):
    '''
    Load data.
    For the reference CCF the path with '.fits' should be specified.
    For the CCFs the pathcan be specified:
            '.fits', if one wish to work with only 1 file
            '.txt', if one wish to work with several fits, the .txt with full paths should be provided
            directory, if one wish to work with all fits from directory
    !! It is important that in current version of code the time of observation check is not implemented yet. The user must sort the data chronologically by himself before starting work!!
    
    Parameters
    ----------
    path_to_reference: string
        Path to the reference CCF file
    path_to_data: string
        Path to the data
    '''

    if os.path.isdir(path_to_reference):
        print("Please, spectify the reference file")
        sys.exit(1)
    elif os.path.isfile(path_to_reference):
        if (path_to_reference[-4:]=='fits'):
            CCF_reference=data_load_fits(path_to_reference)
            
    if os.path.isdir(path_to_data):
        CCF_second=[os.path.join(path_to_data, file) for file in os.listdir(path_to_data)]
    elif os.path.isfile(path_to_data):
        if (path_to_data[-4:]=='fits'):
            CCF_second=data_load_fits(path_to_data)
        else:
            CCF_second=data_load_txt_of_files(path_to_data)
    return CCF_reference,CCF_second
