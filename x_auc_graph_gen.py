#!/usr/bin/env python3

########################################################
#
#  v1  14.03.26  original from Claire Colas
#  v2  19.12.24  updated the code
#
#  generate AUC and log(AUC) figures. Use .svg format for
#  smaller file size
#
########################################################

import sys,os
import matplotlib.pyplot as plt

from math import log10

ranked_lig_list = sys.argv[1]
enr_dud_list    = sys.argv[2]
NAME  = sys.argv[3]
times = sys.argv[4]
imgfm = sys.argv[5]

l, x, y, w = [], [], [], []
j = 0
with open(enr_dud_list, 'r') as fi:
  enr_dud = [line for line in fi]

interval = int( round( float(len(enr_dud))/float(times), 0 ) )

for step in range(0, len(enr_dud), interval):
  line = enr_dud[step]  
  l.append('empty')
  x.append('empty')
  y.append('empty')
  w.append('empty')
  l[j] = line.split(None,2)
  x[j] = round( float(l[j][0]), 0 )
  y[j] = round( float(l[j][1]), 0 )

  if x[j] is 'empty':
    pass
  else:
    if float(x[j]) < 0.01:
      w[j] = log10(0.01)
      pass
    else:
      w[j] = log10(float(x[j]))
      #print w[j]
  j += 1

with open(ranked_lig_list, 'r') as fi:
  for line in fi:
    a = line.split(None,4)

##########################################################################
plt.figure(1, figsize=(10,20))
plt.subplot(211)
plt.suptitle(NAME, fontsize=30)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('% of ranked database',    fontsize=24)
plt.ylabel('% of known ligands found',fontsize=24)
plt.plot(x, y, color='red',  linewidth=3, label='Model')
plt.plot(x, x, color='blue', linewidth=3, label='Random', linestyle='--')
plt.legend(loc=2,prop={'size':18})
plt.text(70, 2, a[0]+' '+a[1], fontsize=24)
plt.savefig('{0}.AUC.{1}'.format(NAME, imgfm), dpi=200)
print('AUC= {0}'.format(a[1]))

#plt.subplot(212)
#plt.xlabel('log % of ranked database')
#plt.ylabel('% of known ligands found')
#plt.plot(w, y, color='red', linewidth=2, label='Model')
#plt.plot(w, x, color='blue', linewidth=2, label='Random')
#plt.legend()
#plt.savefig('enrichment_profile.png', dpi=65)

plt.subplot(212)
plt.xlabel('log(% of ranked database)',    fontsize=24)
plt.ylabel('% of known ligands found',fontsize=24)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.plot(x, y, color='red',  linewidth=3, label='Model')
plt.plot(x, x, color='blue', linewidth=3, label='Random', linestyle='--')
plt.xscale('log')
plt.legend(loc=2,prop={'size':18})
plt.text(1, 80, a[2]+' '+a[3], fontsize=24)
plt.savefig('{0}.AUC.{1}'.format(NAME, imgfm), dpi=200)
print('logAUC= {0}'.format(a[3]))
