from scipy.sparse import *
import numpy as np


def p1_has_cycle(sets):
    A1=csr_matrix(sets)    
    switch=False
    while A1.get_shape()[0] > 1 and not switch:
        is_one=np.where(A1[0].A.T == 1)[0][0]
        is_negone=np.where(A1[0].A.T == -1)[0][0]
        rewireable = np.where(A1.T[is_one].A.T== -1)[0]
        for i in rewireable:
            if np.logical_and((A1.T[is_one].A == -1)[0][i],(A1.T[is_negone].A == 1)[0][i]) :
                switch=True
                break
            else:
                p=A1[0]+A1[i]
                A1=vstack([A1,p])
        A1=A1[1:]
    return switch

