from EPiCA.ccf import CCF_ESPRESSO
import numpy as np

def pc(CCF_reference:float,CCF_second:float,velocity_grid:float)->float:
    '''
    Calculation of RV change according to the Connes 1985 DOI:10.1007/BF00653671 paper.
    Parameters
    ----------
    CCF_reference: attribute 'intensity' of object of class CCF_ESPRESSO
        Array contains reference CCF intensity
    CCF_second: attribute 'intensity' of  object of class CCF_ESPRESSO
            Array contains  CCF intensity
    velocity_grid: attribute 'velocity' of  object of class CCF_ESPRESSO
            Array contains velocity grid of CCF
    '''
    CCF_second_n=CCF_second*sum(CCF_reference)/sum(CCF_second)
    CCF_reference_diff=np.gradient(CCF_reference,velocity_grid)
    re=-(CCF_second_n-CCF_reference)/CCF_reference_diff
    sig=2*CCF_second_n/CCF_reference_diff**2
    weight=1/sig
    weighted_dsp=re*weight/sum(weight)
    return sum(weighted_dsp)
    
