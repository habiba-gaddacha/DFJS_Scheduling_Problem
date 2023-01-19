# Distributed Flexible Job shop Scheduling Problem
### This project is in collaboration with : 
----------------------------------------
II3 IA 2023

- Habiba Gaddacha

- Syrine Bahri

- Cyrine Fekih

- Mehdi Njema
-----------------------------------------

# I - State of the art :

The Distributed and Flexible Job shop Scheduling Problem consists of a set of : 
- factories( F = 1, 2,..., l) 
- set of jobs( N = 1, 2,..., i)
- geographically distributed with a travel time( Dli).
- Each factory has a set of machines.
- Each job i consists of a sequence of Nj operations Oi j, i = ,2,. N; j = ,2,., Nj
- Each operation can be reused on different machine with different processing times(Pijrf). 

The idea of the DFJSP is to associate or allocate to each factory a job while respecting the hypotheses and constraints and also determine the product scheduling
in each plant in order to minimize the maximum completion time (makespan) among all factories. 

In DFJSP, we consider the following hypotheses and constraints :

- 1 - It's generally assumed that each machine can only handle one operation at each time.
- 2 - Each operation can only be reused after its priority operation.
- 3 - Each operation has to be carried out on only one machine.
- 4 - Once a job is allocated to a plant, all of its operations will be reused in that plant.
- 5 - The operations have to be progressed until completion.

# II- Solution proposed :
## Specific solution using 2 machines :
### Output :

![téléchargement (2)](https://user-images.githubusercontent.com/77301851/213435788-8b050ae6-aacf-4fad-9382-8b155dcc5669.png)

## General Solution :
#### * 4 classes :
 1- Class Destributed : Generates initial solution + calculates the makespan + associates firstly each Job to one of the factories
 
 2- Class DFJSP : devide the operations/machines by 50% from the initial solution for the cross-over(in Genetic algorithm afterwards)
 
 3- Class ALL : Applying genetic algorithm to generate new populations for each factoris (epoch = 100) (using mutation & cross-over for operations & factories)
 
 4- Class main : generate the solution ( Gantt chart + makespan of each factory for each epoch (generation) and optimized makespan (best solution for each factory)

### Output :
----------------------------------------------------------------------------------------------------------
![4](https://user-images.githubusercontent.com/78451998/213246000-82df6e22-dd80-4e51-86bc-f0a45280b0d8.png)

![1](https://user-images.githubusercontent.com/78451998/213246008-ceb84ec7-34bd-46f4-aae2-9972141d767a.png)

![2](https://user-images.githubusercontent.com/78451998/213246012-0f0e55c7-eb26-48b2-8836-ce92521a9292.png)

![3](https://user-images.githubusercontent.com/78451998/213246022-7ca54b9f-4f8e-4735-8bad-44342b936d6b.png)

----------------------------------------------------------------------------------------------------------

# Sources :
----------
### 1-  Solving Distributed and Flexible Job shop Scheduling Problem using a Chemical Reaction Optimization metaheuristic by Mr. Bilel Marzoukia, Ms. Olfa Belkahla Driss and Mr. Khaled Ghedira.

Link : https://www.academia.edu/37731969/Solving_Distributed_and_Flexible_Job_shop_Scheduling_Problem_using_a_Chemical_Reaction_Optimization_metaheuristic

### 2-  Solving Distributed and Flexible Job-Shop Scheduling Problems for a Real-World Fastener Manufacturer by Mr. Tung-Kuan Liu, Mr. Yeh-Peng Chen and Mr. Jyh-Horng Chou
Link : https://www.researchgate.net/publication/272171414_Solving_Distributed_and_Flexible_Job-Shop_Scheduling_Problems_for_a_Real-World_Fastener_Manufacturer

