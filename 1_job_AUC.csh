#!/bin/csh

# 14.06.14
#
# calculate the enrichment factor and AUC/logAUC of binding result of
# known ligands from a set of known nonbinders
#
#
if ($#argv != 4)  then
  echo "    Usage: > ${0}"
  echo "          [Ranked Data File] [Known Actives] [AUC Output Prefix]"
  echo "          [Generate PNG figure: 1|0]"
  exit 1
endif

set x = ~/Dropbox/9_scripts/3_program/enrichment
#set x = ~/Documents/Dropbox/9_scripts/3_program/enrichment

echo $x
echo $argv[1]
grep -v '#' $argv[1] | grep -v "Score" > _temp.$argv[1]
$x/x_extract_column.pl _temp.$argv[1] 1 > _temp.$argv[3]
set name = `basename $argv[1] .txt`

$x/x_enrich.py _temp.$argv[3] $argv[2]
$x/x_calc_logauc.py _temp.$argv[3].enr1000.dud > _temp.$argv[3].AUC
echo $name `cat _temp.$argv[3].AUC` >> ALL.AUC.dat

if ($argv[4] > 0) then
  set num = `cat _temp.$argv[3].enr.dud | wc -l`
  $x/x_graph_2.py _temp.$argv[3].AUC _temp.$argv[3].enr.dud $argv[3] $num
endif

rm _temp.$argv[3]* _temp.$argv[1]
