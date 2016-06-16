##My approach to the forth assignment
###Background
Nowadays the mathematical physics equations(ordinary and partial differential euqations) have been playing a significant role in modern science. However, most of them do not have an analytical solution, which emphasises the importance of developing numerical methods to solve these problems. And the lecture made us take the first step into learning such methods.  
**the** **Euler** **Method**:  
As is known to us all, any analytical function, either real or complex, can be written in the form of an infinite series, each term is related to the function's derivatives of order n,which is called Tylar series. To solve the problem numerically,we can pick the 0 order term and the one order term as the approximation.That is the main idea of this method.

###Digest
choose the variables wisely, develop a program to calculate all the data we need and draw a diagram to show the changing process.

###Content
I choose problem 1.5 as the exercise:  
Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are

 where for simplicity we have assumed that the two types of decay are characterized by the same time constant, tau. Solve this system of equation for the numbers of nuclei, NA and NB, as functions of time. Consider different initial conditions, such as NA=100, NB=0, etc, and take tau=1s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.
 
###Calculation of different initial conditions  
![](https://raw.githubusercontent.com/NABLAfai/computationalphysics_N2013301020146/master/4th%201.png)  
NA=80,NB=0,t=1, time interval=0.05  
![](https://raw.githubusercontent.com/NABLAfai/computationalphysics_N2013301020146/master/4th%202.png)  
NA=100,NB=50,t=1, time interval=0.02  
![](https://raw.githubusercontent.com/NABLAfai/computationalphysics_N2013301020146/master/4th%203.png)  
NA=100,NB=30,t=2, time interval=0.03  
[codes](https://raw.githubusercontent.com/NABLAfai/computationalphysics_N2013301020146/master/4th%20homework.py)  
  
All data is shown in the pictures  
###Conclusion  
In general, in this question, no matter what the initial ratio of NA and NB is, the system will eventually reach a stable state where NA=NB=(NA(0)+NB(0))/2. This is consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state that the time derivatives dNA/dt and dNB/dt should vanish which can also be observed from the pictures above.
