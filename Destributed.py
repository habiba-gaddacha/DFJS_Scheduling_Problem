
from random import choice

OS = [1, 3,5, 1,4, 2, 2, 3,4,5] #opérations chaque job posséde 2 opérations
MS = [2, 1,1,3,2, 1, 2, 3,1,2] #machines
Travel_time=[[5,6,4,2,8],[9,5,3,6,5]] #factory1(J1,J2,J3,J4) -same for 2
JS=[1,2,3,4,5] #3*Jobs
# opération 11 -> macchine2 et  opérations 12 -> machine 1
op_times1 = [[5, 4, 4], [4, 2, 3], [2, 2, 1], [3, 4, 3], [5, 4, 5], [2, 9, 2],[4,2,5],[8,1,2],[6,1,3],[4,2,7]] #[5, 4, 5] 5 est l'operation 1 de Job 3 +Machine 3
op_times2 = [[2, 4, 3], [5, 1, 3], [5, 3, 1], [4, 2, 1], [5, 3, 5], [5, 1, 2],[3,4,2],[5,3,8],[6,1,6],[4,3,5]]
"""The initial solution algorithm consists in affect firstly the different jobs to all factories using a heuristic which
consists in scheduling the current job in a each factory, then we choose the best scheduling"""
def Pijrf(i,f,r,op):
    if f==0 :
        #op_times1
      if i==1:
          return op_times1[0:2][op][r-1]
      if i==2:
          return op_times1[2:4][op][r - 1]
      if i==3:
          return op_times1[4:6][op][r - 1]
      if i==4:
          return op_times1[6:8][op][r - 1]
      if i==5:
          return op_times1[8:][op][r - 1]
    else :
        if i == 1:
            return op_times2[0:2][op][r - 1]
        if i == 2:
            return op_times2[2:4][op][r - 1]
        if i == 3:
            return op_times2[4:6][op][r - 1]
        if i==4:
            return op_times2[6:8][op][r - 1]
        if i==5:
            return op_times2[8:][op][r - 1]


def  Generate_initial_solution():
    date_deb=[0,0] #factory 1 factory 2
    date_fin=[0,0]
    F1 = []
    F2 = []
    MF1=[]
    MF2=[]
    for i in JS:#on choisis un job
             # on choisit une factory
                 f = choice([0, 1])
                 if f == 0:
                        F1.append(i)
                        for op in range(0,2) : #0=job11 / 1= job12
                                r = choice(MS)  # 1 2 3
                                MF1.append([op,r])
                        #print("F1",F1,"  MF1",MF1)

                 else:
                        F2.append(i)
                        for op in range(0, 2):  # 0=job11 / 1= job12
                            r = choice(MS)  # 1 2 3
                            MF2.append([op, r])
                            #print("F2", F2, "  MF2", MF2)
                 if Pijrf(i, f, r,op) !=0 :
                            date_fin[f]=date_deb[f]+Pijrf(i, f, r,op) # i = job i / j=opération  Pij=O11 ou O12
                            date_deb[f]=date_fin[f]
                 date_fin[f] = date_fin[f] + Travel_time[f][i-1]

    """if date_fin[0]<=date_fin[1]:
          print(date_fin)
          return (0,date_fin[0])
    else :
        print(date_fin)
        return (1,date_fin[1])"""
    #f1
    if len(F1) == 5 and len(F2) == 0:
        F2 = F1[0:2]
        F1.remove(F1[0])
        F1.remove(F1[0])
        MF2 = MF1[0:4]
        MF1.remove(MF1[0])
        MF1.remove(MF1[0])
        MF1.remove(MF1[0])
        MF1.remove(MF1[0])
    if len(F2) == 5 and len(F1) == 0:
        F1 = F2[0:2]
        F2.remove(F2[0])
        F2.remove(F2[0])
        MF1 = MF2[0:4]
        MF2.remove(MF2[0])
        MF2.remove(MF2[0])
        MF2.remove(MF2[0])
        MF2.remove(MF2[0])
    if len(F1) == 4 and len(F2) == 1:
        F2.append(F1[0])
        F1.remove(F1[0])
        MF2.append(MF1[0:2][0])
        MF2.append(MF1[0:2][1])
        MF1.remove(MF1[0])
        MF1.remove(MF1[0])
    if len(F2) == 4 and len(F1) == 1:
        F1.append(F2[0])
        F2.remove(F2[0])
        MF1.append(MF2[0:2][0])
        MF1.append(MF2[0:2][1])
        MF2.remove(MF2[0])
        MF2.remove(MF2[0])
    print("_________ SUMMARY___________")
    print("  ")
    print(
'''Hypotheses and constraints: 
(1) It is generally assumed that each machine can only handle one operation at each time;
(2) Each operation can only be processed after its precedence operation; 
(3) Each operation has to be carried out on
only one machine; 
(4) Once a job is allocated to a factory, all of its operations will be processed in that factory; 
(5) The operations have to be proceeded until completion. ''' )
    print("F1",F1)
    for i in range(len(F1)):
        print("Job ",i+1," is Job ",F1[i])
    print("F2",F2)
    for i in range(len(F2)):
        print("Job ",i+1," is  Job ",F2[i])
    print("MF1",MF1)
    print("MF2",MF2)
    print("______________________________")

    return F1,F2,MF1,MF2,date_fin[0],date_fin[1]
