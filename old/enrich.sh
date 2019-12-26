#!/bin/bash

##
##  Got from Claire Colas
##
##  v1.  14.03.26
##
##  original shell script to calculate the enrichment of docking result
##  superseded by the python version x_enrich.py for better readability
##

USAGE="ERROR:
This script calculates AUC curves from two input files:
1) the docking compounds ranked and 2) the active compounds."

if [[ $# -lt 2 ]] ; then

  echo "$USAGE"
  exit 1
  
fi

dataSet=$1
activeSet=$2


dataNb=`less $dataSet | grep -v '^$' | wc -l | LANG=C awk '{print $1}'`
echo "Total : $dataNb"

activeNb=`less $activeSet | grep -v '^$' | wc -l | LANG=C awk '{print $1}'`
echo "Active : $activeNb"

inactiveNb=`expr $dataNb - $activeNb`
echo "Inactive : $inactiveNb"

increment=`echo $dataNb | LANG=C awk '{print 1/$1}'`
# increment=`echo $inactiveNb | LANG=C awk '{print 1/$1}'`
#echo "increment : $increment"

logincr=`echo $increment | LANG=C awk '{print log($1)}'`


col1=""
col2=""
coordinates=""
activesFound=0
activesNotFound=0
inactivesFound=0
inactivesNotFound=0
testauc=0
auc=0
logauc=0
toto=0
count=1
echo "0.00 0.00" > ${1}.enr1000.dud
echo "0.00 0.00" > ${i}.enr.dud
while [[ $count -le $dataNb ]] ; do

  item=`less $dataSet | sed -n "$count"p`
#   echo "item : $item"
    
  if [[ $count -le $activeNb && "`less $activeSet | grep -w $item`" != "" ]] ; then
    activesFound=`expr $activesFound + 1`
  elif [[ $count -gt $activeNb && "`less $activeSet | grep -w $item`" != "" ]] ; then
    activesNotFound=`expr $activesNotFound + 1`
  elif [[ $count -le $activeNb && "`less $activeSet | grep -w $item`" == "" ]] ; then
    inactivesNotFound=`expr $inactivesNotFound + 1`
  elif [[ $count -gt $activeNb && "`less $activeSet | grep -w $item`" == "" ]] ; then
    inactivesFound=`expr $inactivesFound + 1`
    
  fi

  #echo $activesFound $activesNotFound
  #echo $activesNotFound
  #echo $activesFound $activesNotFound >>  enr.dud
  #echo $count $increment >> enr.dud 
  #echo "LANG=C awk '{printf("%.2f\t%.2f\n", '$count*$increment'*100, '$activesFound/$dataNb'*100)}'" >> enr.dud
  dat=`echo "$count $dataNb $activesFound $activesNotFound $activeNb" | LANG=C awk '{printf("%.2f\t%.2f\n", ($1/$2)*1000, (($3+$4)/$5)*100)}'`
  echo $dat >> ${1}.enr1000.dud
  dat=`echo "$count $dataNb $activesFound $activesNotFound $activeNb" | LANG=C awk '{printf("%.2f\t%.2f\n", ($1/$2)*100, (($3+$4)/$5)*100)}'`
  echo $dat >> ${1}.enr.dud
  count=`expr $count + 1`
done
