#!/bin/csh

## calculate the AUC and log(AUC) of the supplied data

../1_job_AUC.csh     \
  ranked_data.txt    \
  known_actives.txt  \
  performance_auc    \
  svg                \
"/Users/pmung/Dropbox (Schlessinger lab)/9_scripts/3_program/enrichment"


## ranked_data.txt
#  all result in ranked order
#
## known_actives.txt
#  those that are deemed to be active
#
## ranked_data.AUC.dat  ranked_data.AUC
#  saved numeric AUC and logAUC values
#
## ranked_data.enr.dud  ranked_data.enr1000.dud
#  enrichment plot data in long format
#
## performance_auc.AUC.svg
#  AUC and log(AUC) graphs
#
#  19.12.24
