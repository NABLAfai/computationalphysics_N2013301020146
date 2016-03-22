# computationalphysics_N2013301020146
Homework of Computational Physics course of WHU

All the assignments distributed by the teacher Hao Cai by far:  
Link:  
[第一次作业](https://github.com/caihao/computational_physics_whu/blob/master/Exercises.md#第一次作业)  
[第二次作业](https://github.com/caihao/computational_physics_whu/blob/master/Exercises.md#第二次作业)  
[第三次作业](https://github.com/caihao/computational_physics_whu/blob/master/Exercises.md#第三次作业)  
[第四次作业](https://github.com/caihao/computational_physics_whu/blob/master/Exercises.md#第四次作业)

##My approach to the second assignment
###Background
after learning the grammar of Python, the teacher asked us to write a small program which can show letters composed of notations such as "#".

###Digest
the core of the following program are dictionary and 2 dimension array

###Content
https://github.com/NABLAfai/computationalphysics_N2013301020146/blob/master/print%20letters.py  
can't do level 3 now even after referring to some materials, will try it later.

###Reference
some techniques are under instructions of my roommate Chenfeng

##My approach to the forth assignment
###Background
Nowadays the mathematical physics equations(ordinary and partial differential euqations) have been playing a significant role in modern science. However, most of them do not have an analytical solution, which emphasises the importance of developing numerical methods to solve these problems. And the lecture made us take the first step into learning such methods.  
**the** **Euler** **Method**:  
As is know to us all, any analytical function, either is real or complex, can be written in the form of an infinite series, each term is related to the function's derivatives of order n,which is called Tylar series. To solve the problem numerically,we can pick the 0 order term and the one order term as the approximation.That is the main idea of this method.

###Digest
choose the variables wisely, develop a program to calculate all the data we need and draw a diagram to show the changing process.

###Content
I choose problem 1.5 as the exercise:  
Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are

 where for simplicity we have assumed that the two types of decay are characterized by the same time constant, tau. Solve this system of equation for the numbers of nuclei, NA and NB, as functions of time. Consider different initial conditions, such as NA=100, NB=0, etc, and take tau=1s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.  
 codes:  
 `na=float(raw_input('The initial number of nucleiA: '))`  
 `nb=float(raw_input('The initial number of nucleiB: '))`  
 `t=float(raw_input('The initial number of time: '))`  
 `dt=float(raw_input('The time step is: '))`  
 `naa=[na]`  
 `nbb=[nb]`  
 `tt=[t]`

  `for i in range(200):`  
  `    na_temp=nna[-1]+(nnb[-1]-nna[-1])*dt`  
  `    nb_temp=nnb[-1]+(nna[-1]-nnb[-1])*dt`  
  `    t_temp=tt[-1]+dt`  
  `    nna.append(nna_temp)`  
  `    nnb.append(nnb_temp)`  
  `    tt.append(tt_temp)`
  
my matplotlib plugin is still under test,and there are small problems when typing code directly on github, i'll manage to fix these and complete the diagram in no time.

###Clusion
the numerical method is pretty convinient and feasible.


