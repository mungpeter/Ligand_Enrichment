#!/usr/bin/env python3

import sys,os
import pylab
from math import log10

ranked_lig_list = sys.argv[1]
enr_dud_list    = sys.argv[2]
NAME = sys.argv[3]
times = sys.argv[4]

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
pylab.figure(1, figsize=(10,20))
pylab.subplot(211)
pylab.suptitle(NAME, fontsize=30)
pylab.tick_params(axis='x', labelsize=20)
pylab.tick_params(axis='y', labelsize=20)
pylab.xlabel('% of ranked database',    fontsize=24)
pylab.ylabel('% of known ligands found',fontsize=24)
pylab.plot(x, y, color='red',  linewidth=3, label='Model')
pylab.plot(x, x, color='blue', linewidth=3, label='Random', linestyle='--')
pylab.legend(loc=2,prop={'size':18})
pylab.text(70, 2, a[0]+' '+a[1], fontsize=24)
pylab.savefig('{0}.enrich.svg'.format(NAME), dpi=200)
print('AUC= {0}'.format(a[1]))

#pylab.subplot(212)
#pylab.xlabel('log % of ranked database')
#pylab.ylabel('% of known ligands found')
#pylab.plot(w, y, color='red', linewidth=2, label='Model')
#pylab.plot(w, x, color='blue', linewidth=2, label='Random')
#pylab.legend()
#pylab.savefig('enrichment_profile.png', dpi=65)

pylab.subplot(212)
pylab.xlabel('log(% of ranked database)',    fontsize=24)
pylab.ylabel('% of known ligands found',fontsize=24)
pylab.tick_params(axis='x', labelsize=20)
pylab.tick_params(axis='y', labelsize=20)
pylab.plot(x, y, color='red',  linewidth=3, label='Model')
pylab.plot(x, x, color='blue', linewidth=3, label='Random', linestyle='--')
pylab.xscale('log')
pylab.legend(loc=2,prop={'size':18})
pylab.text(1, 80, a[2]+' '+a[3], fontsize=24)
pylab.savefig('{0}.enrich.svg'.format(NAME), dpi=200)
print('logAUC= {0}'.format(a[3]))
