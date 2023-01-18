import random
import numpy as np
from ALL import genetics
from DFJSP import  OS
from Destributed import Generate_initial_solution


""" Inputs """

op_times2 = [[2, 4, 3], [5, 1, 3], [5, 3, 1], [4, 2, 1], [5, 3, 5], [5, 1, 2], [3, 4, 2], [5, 3, 8], [6, 1, 6],
             [4, 3, 5]]
op_times1 = [[5, 4, 4], [4, 2, 3], [2, 2, 1], [3, 4, 3], [5, 4, 5], [2, 9, 2], [4, 2, 5], [8, 1, 2], [6, 1, 3],
             [4, 2, 7]]  # [5,4, 5] 5 est l'operation 1 de Job 3 +Machine 3
F1,F2,MF1,MF2,date_fin1,date_fin2=Generate_initial_solution()
print("-------------------------------------------------------------------------- BEGIN GANTT CHART----------------------------------------------------------------------------")

print("************Factory1************")
print("----START----")
OS1,OS_P1,OS_P2,MS_P1,MS_P2=OS(F1,MF1)
genetics(OS1,F1,op_times1)
print("----END----")
print("************Factory2************")
print("----START----")
OS2,OS_P1,OS_P2,MS_P1,MS_P2=OS(F2,MF2)
genetics(OS2,F2,op_times1)
print("----END----")
print("-------------------------------------------------------------------------- END GANTT CHART----------------------------------------------------------------------------")
print("")
print("")

print("~~~~~~MAKESPAN  Factory 1~~~~~~")
print(date_fin1)
print("")
print("~~~~~~MAKESPAN  Factory 2~~~~~~")
print(date_fin2)





