#!/bin/csh

#
# Peter MU Ung @ MSSM
#
# v1   14.06.14
# v2   19.12.25  updated, remove perl script dependency
#
# calculate the enrichment factor and AUC/logAUC of binding result of
# known ligands from a set of known nonbinders
#
#
if ($#argv != 5)  then
  echo ""
  echo "    > ${0}"
  echo "         [ Ranked Data File: .txt ]  * only use name in 1st col, no header"
  echo "         [ Known Actives:    .txt ]  * only use name in 1st col, no header"
  echo "         [ AUC Output Prefix      ]"
  echo "         [ figure format: png|svg ]" 
  echo "         [ Script location        ]" 
  echo ""
  exit 1
endif

set script = "$argv[5]"

echo $script
echo $argv[1]
echo $argv[4]
set name_pref = `basename $argv[1] .txt`

## Calculate enrichment data, use that to calc AUC and log(AUC) values
"$script/x_calc_enrich.py"     \
  $argv[1]                     \
  $argv[2]

"$script/x_calc_logauc.py"     \
  $name_pref.enr1000.dud       \
    > $name_pref.AUC
echo $name_pref `cat $name_pref.AUC` >> $name_pref.AUC.dat



## Generate AUC figure
set num = `cat $name_pref.enr.dud | wc -l`

"$script/x_auc_graph_gen.py"   \
  $name_pref.AUC               \
  $name_pref.enr.dud           \
  $argv[3]                     \
  $num                         \
  $argv[4]

