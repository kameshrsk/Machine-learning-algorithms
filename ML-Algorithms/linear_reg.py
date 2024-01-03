import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def cost_function(x,y,w,b):
    m=len(x)
    j=0
    for i in range(m):
        j+=(w*x[i]+b-y[i])**2
    j=j/(2*m)
    
    return j

def compute_gradient(x,y,w,b):
    d_dw=0
    d_db=0
    m=len(x)
    for i in range(m):
        f_wb=w*x[i]+b
        d_db+=f_wb-y[i]
        d_dw+=(f_wb-y[i])*x[i]
    d_db=d_db/m
    d_dw=d_dw/m
    return d_dw, d_db

def gradient_descent(x,y,w,b,iters):
    alpha=0.000001
    j=[]
    wl=[]
    prev_cost=cost_function(x,y,w,b)
    for i in range(iters):
        w_gradient,b_gradient=compute_gradient(x,y,w,b)
        w=w-(alpha*w_gradient)
        b=b-(alpha*b_gradient)
        curr_cost=cost_function(x,y,w,b)
        j.append(curr_cost)
        wl.append(w)
        if(abs(prev_cost-curr_cost)<1e-7):
            break
        prev_cost=curr_cost
    return w,b, j,wl


x = [2000, 2100, 2500, 2250, 3000, 1900, 1500, 1850, 2700, 2100, 2150, 2100, 2100, 2510, 2250, 3100, 1800, 1550, 1800, 2700, 2110, 2100, 3500, 1200, 2800, 3100, 2750, 1800, 2200, 3100, 2100, 2100, 2500, 2250, 3000, 1900, 1500, 1850, 2700, 2100, 2150, 2100, 2100, 2510, 2250, 3100, 1800, 1550, 1800, 2700, 2110, 2100, 3500, 1200, 2800, 3100, 2750, 1800, 2200, 3100]
y= [31500, 35000, 41050, 36100, 52100, 32500, 20000, 24500, 48000, 31000, 34500, 32000, 34500, 40050, 34100, 51500, 30500, 21000, 25000, 47000, 31500, 33500, 70000, 20000, 50000, 53000, 48000, 25000, 31460, 51400, 33500, 35010, 41100, 35100, 52200, 32300, 20200, 24000, 47500, 31500, 34400, 32020, 34700, 40000, 35000, 51000, 30000, 21500, 25500, 47500, 31000, 33000, 70500, 20100, 51000, 54000, 48500, 25100, 31560, 51600]
plt.scatter(x,y)
plt.show()
x=x/np.max(x)
y=y/np.max(y)

w=0.25
b=0.25

w,b,j,wl=gradient_descent(x,y,w,b,100000)

x_input=float(input("Enter house size: "))
print("The w and b is: ",w,b)
prediction= (w*x_input)+b
print("Number of Iterations: ",len(j))
print("The predicted rent is: ",prediction)
