# -*- coding: utf-8 -*-
"""

FunctionPractice
Created on Sat Jan  2 15:39:29 2021

@author: dsudds1963
"""

# def Function(Input):
#     actions
#     return Output

def addOne(Number):
    Number += 1
    return Number


Var = 0 
Var2 = addOne(Var)
Var3 = addOne(Var2)
Var4 = addOne(2.1+3.4)

print (Var)
print (Var2)
print (Var3)
print (Var4)

def addOneAddTwo (NumberOne,NumberTwo):
    Output = NumberOne + 1
    #Output = Output + NumberTwo +2
    Output += NumberTwo + 2
    return Output

Sum = addOneAddTwo (Var2, Var3)

print (Sum)

