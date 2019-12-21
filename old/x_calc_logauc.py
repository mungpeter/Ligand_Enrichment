#!/usr/bin/env python3

import sys, os
import numpy as np
from numpy import trapz
from math import log10, log
from scipy.integrate import trapz
#DB = sys.argv[1]

DUD = sys.argv[1]
f = open(DUD,"r")

malistey = [] 
malistex = []
malistex2 = []
lines = f.readlines()

#print( lines)

for i in lines:
#  print( i)
  splited=i.split()
  xla=float(splited[0])
  xla2=float(splited[0])/1000
  #print( xla, xla2)
  if float(xla) < 0.01:
     xl1=log10(0.01)
     #pass
  else:
      xl1=log10(xla)
  #print( xl1)
  #print( xla, xla2, xl1)
  xl2=xl1/3
  #print( xl2)
  yla=float(splited[1])
  #print( yla)
  
  malistey.append(yla)
  malistex.append(xl2)
  malistex2.append(xla2)

area=trapz(malistey,malistex)
area2=trapz(malistey,malistex2)
print("AUC= {0:.3f}  logAUC= {1:.3f}".format(area2,area))



f.close()  
  
