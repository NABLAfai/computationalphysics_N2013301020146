import time

for i in range(10):
    startT = time.clock()
    k=float(10**(2*i))
    c=((k-1)/(k+1))
    d=(2/(k+1))
    v_an=[1]
    v_bn=[0]
    while True:  
    
        v_ai=c*v_an[-1]-d*v_bn[-1]
        v_bi=(2*c+d)*v_an[-1]+c*v_bn[-1]
        v_an.append(v_ai)
        v_bn.append(v_bi)
        if abs(v_an[-1])>abs(v_bn[-1])and v_an[-1]<=0:
                break
        endT = time.clock()
    if v_bn[-1]>0:
        pi=float(2*(len(v_an)-1))
    else:
        pi=float(2*(len(v_an)-1)-1)
    print pi/10**i
    print "%.10f"%(endT-startT)
    print "-"*15
    
    


    
    