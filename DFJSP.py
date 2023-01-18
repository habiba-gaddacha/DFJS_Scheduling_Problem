import random
import numpy as np
from Destributed import Generate_initial_solution

def OS(F,MF):
    OS = []
    MS = []
    k=0
    for i in F:  # 1 [1,3]
        for a in range(2):
            OS.append(i)  # opérations chaque job posséde 2 opérations
            MS.append(MF[k][1])  # machines
            MF.remove(MF[k])

    """ OS = [1, 3, 1, 2, 2, 3] #opérations chaque job posséde 2 opérations
    MS = [2, 1, 3, 1, 2, 3] #machines"""
    # opération 11 -> macchine2 et  opérations 12 -> machine 1
    OS1=OS.copy()
    OS2=OS.copy()
    MS1=MS.copy()
    MS2=MS.copy()
    random.shuffle(OS1)
    random.shuffle(OS2)
    random.shuffle(MS1)
    random.shuffle(MS2)
    OS_P1=OS1
    OS_P2=OS2
    MS_P1=MS1
    MS_P2=MS2
    return  OS,OS_P1,OS_P2,MS_P1,MS_P2
