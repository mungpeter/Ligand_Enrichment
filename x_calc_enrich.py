#!/usr/bin/env python3

####################################################################
#
#  v1   14.03.26  Original from Clair Colas as "enrich.sh"
#  v2   14.06.04  Rewritten by Dane Hillard, 4 June 2014
#  v3   19.12.25  Updated to handle parsing internally
#
#  This script calculates AUC curves from the specified input files.
#  In addition, enrichment factor (EF) at different subset ratios is
#  also calculated.
#
####################################################################
import sys,re
import gzip,bz2
import numpy as np
import pandas as pd

usage_message = """
  Usage: enrich.py 
      [ ranked docking compounds file: .txt ] # use 1st col; no header
      [ active compounds file:         .txt ] # use 1st col; no header\n
This script calculates AUC curves from the specified input files.
In addition, enrichment factor (EF) at different subset ratios is
also calculated.
"""
if len(sys.argv) < 3: sys.exit(usage_message)

data_set_file_name   = sys.argv[1]
active_set_file_name = sys.argv[2]

data_set_file_pref   = data_set_file_name.split('.txt')[0]
#########################################################################

## Read in files
rdf = pd.read_csv(data_set_file_name, header=None, delimiter='\s+', comment='#').dropna()
Data_Set = rdf.iloc[:,0].tolist()
data_set_count = float(len(Data_Set))
print('Ranked input file: {}\n'.format(int(data_set_count)))

kdf = pd.read_csv(active_set_file_name, header=None, delimiter='\s+', comment='#').dropna()
Active_Set = kdf.iloc[:,0].tolist()
active_count = float(len(Active_Set))
print('Known active file: {}\n'.format(int(active_count)))

## Calculate enrichment subsets in different ranges
active_ratio = np.divide(active_count, data_set_count)
Subsets = [[int(round(data_set_count * 0.01)), 1 ],
           [int(round(data_set_count * 0.05)), 5 ],
           [int(round(data_set_count * 0.10)), 10],
           [int(round(data_set_count * 0.15)), 15],
           [int(round(data_set_count * 0.20)), 20],
           [int(round(data_set_count * 0.25)), 25],
           [int(round(data_set_count * 0.50)), 50],
           [int(round(data_set_count * 0.99)),100] ]

print('Total : {0}\nActive : {1}\nInactive : {2}\n'.format(
        data_set_count, active_count, data_set_count - active_count))

with open('{0}.enr.dud'.format(data_set_file_pref), 'w') as output_dud:
  with open('{0}.enr1000.dud'.format(data_set_file_pref), 'w') as output_dud_1000:
      output_dud.write('0.00 0.00\n')		
      output_dud_1000.write('0.00 0.00\n')		

      EF_active_found  = 0.0
      active_found     = 0.0
      active_not_found = 0.0
      Active_Found     = []

      for data_set_index, compound in enumerate(Data_Set):
        Name = compound.split()

        if data_set_index <= active_count and Name[0] in Active_Set:
          active_found += 1.0
        elif data_set_index > active_count and Name[0] in Active_Set:
          active_not_found += 1.0

        ## For enrichment factor calculation
        if Name[0] in Active_Set:
          EF_active_found += 1.0
          Active_Found.append(Name[0])

        # Calculate the Enrichment factor at certain subset ratio
        for Subset in Subsets:
          if data_set_index == Subset[0]:
            EF = float(EF_active_found / data_set_index) / active_ratio
            print('  EF at {0} %: {1:.2f}'.format(Subset[1], EF))

        rank_ratio = data_set_index / float(data_set_count)
        found_not_found_ratio = ((active_found + active_not_found) / float(active_count)) * 100

        output_dud.write('{0:.2f} {1:.2f}\n'.format(
                         rank_ratio * 100,found_not_found_ratio))

        output_dud_1000.write('{0:.2f} {1:.2f}\n'.format(
                              rank_ratio * 1000, found_not_found_ratio))
      Not_Found = list(set(Active_Set)-set(Active_Found))
      if len(Not_Found) > 0: 
        print('The following \'Known(s)\' is not found in the dataset')
        print(Not_Found)
