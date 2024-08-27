#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:30:11 2024

@author: sudipto3331
"""

from matplotlib import pyplot as plt
import math
import numpy as np
a2=float(input("Enter the value of a2 FOR USING, euler a2=0,for heuns a2=0.5,for midpoint a2=1 "))
a1=float(input("Enter the value of a1 FOR USING, euler a1=1,for heuns a1=0.5,for midpoint a1=0"))
order=int(input("Enter the value of order :"))
def f(x,y):
   fxy=(-4*(x**3)+12*(x**2)-20*x+8.5)
   return fxy

x0=float(input("Enter the lower range of x: " ))
xfinal=float(input("Enter the higher range of x: " ))
y0=float(input("Enter the lower range of y: " ))
h=float(input("Enter the step size: "))
n=int(((xfinal-x0)/h)+1)
x=np.zeros([n+1])
y=np.zeros([n+1])
k1=np.zeros([n+1])
k2=np.zeros([n+1])
k3=np.zeros([n+1])
k4=np.zeros([n+1])
x[0]=x0
y[0]=y0
for i in range(n):
    x[i+1]=x[i]+h
if all([a1==1,a2==0,order==1]):
    print("Euler method :")
for i in range(n):
        y[i+1]=y[i]+h*f(x[i],y[i])
print(y)
if all([a1==.5,a2==.5,order==2]):
    print("Heuns method :")
    for i in range(n):
      k1[i+1]=f(x[i],y[i])
      k2[i+1]=f(x[i]+h,(y[i]+k1[i+1]*h))
      y[i+1]=y[i]+h/2*(k1[i+1]+k2[i+1])
    print(y[i+1])
if all([a1==0,a2==1,order==2]):
    print("Midpoint method :")
    for i in range(n):
        k1[i+1]=f(x[i],y[i])
        k2[i+1]=f(x[i]+h/2,(y[i]+k1[i+1]*h/2))
        y[i+1]=y[i]+k2[i+1]*h
    print(y[i+1])
if order==4:
    print("forth order rk method :")
for i in range(n):
    k1[i+1]=f(x[i],y[i])
    k2[i+1]=f(x[i]+h/2,(y[i]+k1[i+1]*h/2))
    k3[i+1]=f(x[i]+h/2,(y[i]+k2[i+1]*h/2))
    k4[i+1]=f(x[i]+h,(y[i]+k1[i+1]*h))
    y[i+1]=y[i]+(h/6)*(k1[i+1]+2*k2[i+1]+2*k3[i+1]+k4[i+1])
    print(y)
    
plt.figure(1)
plt.plot(x,y)
plt.xlabel('Values of X')
plt.ylabel('Values of Y')
plt.title('Curve Of the ODE')
plt.legend(['Graphcal Curve '], loc='upper right')
plt.plot(x,y)
plt.show()
