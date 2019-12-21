#!/bin/csh

# 14.06.10
#
# batch mode to run job_AUC.csh, which calculates the enrichment factor
# and AUC/logAUC of the known binder docking results from known nonbinders
#
# supply a list of ranked docking results and known binders of the protein
# to calculate AUC for each individual docking result on the list
#

if ($#argv != 2)  then
  echo "    Usage: > ${0}"
  echo "          [filename key word] [Known Actives]"
  echo "     e.g.: score.list x.known.list "
  exit 1
endif

set x = ~/Dropbox/9_scripts/3_program/enrichment
set known = $argv[2]

foreach txt (`cat $argv[1]`)

  set prefix = `basename $txt .txt`
  $x/1_job_AUC.csh $txt $known $prefix 1

end
