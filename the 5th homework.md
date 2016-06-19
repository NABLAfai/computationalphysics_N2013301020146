## Abstract ##  
Solve the problem 1.1 and draw the picture with matplolib  
## Background ##  
In Newtonian physics, free fall is any motion of a body where gravity is the only force acting upon it. In the context of 
general relativity, where gravitation is reduced to a space-time curvature, 
a body in free fall has no force acting on it and moves along a geodesic.  
#Main#  
The image of the velocity-time in free fall motion:  
![](https://raw.githubusercontent.com/NABLAfai/computationalphysics_N2013301020146/master/5th%201.png)  

codes:  
````  
rom pylab import *

v=[]
t=[]
dt=0.1
g=9.8

v.append(0.)
t.append(0)
end_time=10

for i in range(int(end_time/dt)):
    u=v[i]+g*dt
    v.append(u)
    t.append(dt*(i+1))
    print t[-1],v[-1]
    
plot(v,t)
title('Velocity-time')
xlabel('t(s)')
ylabel('v(m/s)')

show()  
````  
## Conclusion ##  
The free fall motion is a uniformly accelerated motion.  
## Reference ##  
The teacher's codes.
