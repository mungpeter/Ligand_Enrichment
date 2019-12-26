#!/usr/bin/env python3

import sys, os
import numpy as np
import pandas as pd

###########################################################
##
##  Peter MU Ung
##
##  v1  14.03.26  original from Claire Colas
##  v2  19.12.21  rewritten for different approaches
##
##  This script calculates the AUC and log(AUC) values of the 
##  ranked data.
##  in practice, all 3 methods take the same amount of time
##  because the bottleneck for calculation is somewhere else
##
###########################################################

## All-pandas approach, too much pandas overhead. 1000 data ~ 5.20 ms
def slowest_method(inf):
  df = pd.read_csv(inf, header=None, comment='#', sep='\s+').dropna()
  df.columns = ['xla', 'yla']
  df['xla2'] = df.xla.to_numpy()/1000

  df['xl1'] = np.log10(df.xla.to_numpy())
  df.loc[ (df.xla < 0.01), 'xl1'] = np.log10(0.01)

  df['xl2'] = df.xl1.to_numpy()/3.

  area  = np.trapz(df.yla.to_numpy(), df.xl2.to_numpy() )
  area2 = np.trapz(df.yla.to_numpy(), df.xla2.to_numpy())

  return area, area2


#########################################################
## Mixed approach, some overhead. 1000 data ~ 4.00 ms
def slow_method(inf):
  df = pd.read_csv(inf, header=None, comment='#', sep='\s+').dropna()
  data_x2 = df[0].to_numpy()/1000
  data_y  = df[1].to_numpy()

  xl1 = []
  for i in df[0].to_numpy():
    if i < 0.01:
      x = np.log10(0.01)
    else:
      x = np.log10(i)
    xl1.append(x)
  data_x = np.array(xl1)/3

  area  = np.trapz(data_y, data_x )
  area2 = np.trapz(data_y, data_x2)

  return area, area2


########################################################
## Purely python approach. No overhead. 1000 data ~ 2.88 ms
def faster_method(inf):
  
  f = open(inf,"r")

  data_y  = []
  data_x  = []
  data_x2 = []
  lines = f.readlines()

  for line in lines:
    tmp  = line.split()
    xla  = float(tmp[0])
    xla2 = float(tmp[0])/1000
    if float(xla) < 0.01:
      xl1 = np.log10(0.01)
    else:
      xl1 = np.log10(xla)
    xl2 = xl1/3
    yla = float(tmp[1])

    data_y.append(yla)
    data_x.append(xl2)
    data_x2.append(xla2)

  area  = np.trapz(data_y, data_x)
  area2 = np.trapz(data_y, data_x2)
  f.close()
  return area, area2

################################################

area, area2 = faster_method(sys.argv[1])
print("AUC= {0:.3f}  logAUC= {1:.3f}".format(area2,area))

