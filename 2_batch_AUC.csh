#!/bin/csh

# 14.06.10
#
# batch mode to run job_AUC.csh, which calculates the enrichment factor
# and AUC/logAUC of the known binder docking results from known nonbinders
#
# supply a list of ranked docking results and known binders of the protein
# to calculate AUC for each individual docking result on the list
#

if ($#argv != 4)  then
  echo ""
  echo "    Usage: > ${0}"
  echo "          [ List of Ranked Data '.txt' Files ]"
  echo "          [ Known Actives:              .txt ]"
  echo "          [ Figure format:           png|svg ]"
  echo "          [ Directory of scripts             ]"
  echo ""
  echo " e.g.> ${0}  score.list  known_actives.txt "
  echo ""
  exit 1
endif

set script = "$argv[4]"
set known  = $argv[2]
set imgfm  = $argv[3]

## Loop thru list of data files
foreach txt (`cat $argv[1]`)
  set prefix = `basename $txt .txt`

  $script/1_calc_AUC.csh \
    $txt                 \
    $known               \
    $prefix              \
    $imgfm


end
