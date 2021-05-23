#!/usr/bin/env python
# coding: utf-8

# # Решить уравнение методом полного дифференциала
# 
# $$ y-xy^{'}=3(1+x^2y^{'}) $$

# Честно говоря, я не совсем понял как делать это задание, так как оно не решается методом полного дифференциала(условия не выполняются).
# 
# Я понял это задание так: нужно найти значение $у$ при любом значении $х$, т.е. есть решение дифференциального уравнения, задаем через него у, из уравнения вычисляем $y^{'}$ нужно найти такое $С$, чтобы при вычитании из правой части левую мы получали 0 с погрешностью $Е$, тем самым можно найти значение $у$

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


# In[10]:


E=10**-12


# In[11]:


def f(x,C,h):
    def dy(x,C): #y'
        return (ydiff(x,C)-3)/(3*x**2+x)
    def ydiff(x,C): #y решеный с помощью диф. уравнения
        return 3*(C*x+3*x+1)/(3*x+1)
    def perdipari(x,C): # левая часть уравнения
        return ydiff(x,C)-x*dy(x,ydiff(x,C))
    def vtor(x,C): #правая часть уравнения
        return 3*(1+np.power(x,2)*dy(x,ydiff(x,C)))
    
    
    while(abs(vtor(x,C)-perdipari(x,C))>E):
        if((vtor(x,C)-perdipari(x,C)<E)):
            h=h/2
        if((vtor(x,C)-perdipari(x,C)>E)):
            C=C+h
    return C,ydiff(x,C),dy(x,C)


# In[12]:


t=5
Coup=20
honda=0.1
print(f(t,Coup,honda))
Co,y,j=f(t,Coup,honda)
print("Константа С=",Co)
print("Значение y=",y)
print("При x=",t)


# In[13]:


tt=y-t*j-3*(1+np.power(t,2)*j)
print("Значение разности правой части и левой функции=",tt)

