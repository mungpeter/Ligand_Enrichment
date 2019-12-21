#!/bin/csh

##
##	Peter M.U. Ung @ MSSM
##
##	16.05.13	updated
##	
##	aggregate the results from 2 different sets of data for AUC
##	use with run_fred.csh and run_aug_gen.csh

if ($#argv != 5) then
  echo ''
  echo '  Usage: x.csh [list of new files]' 
  echo '               [path to old files]'
  echo '               [sufflix to remove in new files]'
  echo '               [sufflix of OLD files]'
  echo '               [sufflix for aggregated files]'
  echo ''
  echo '   e.g.: x.csh lig.list ../../old  docked.txt docked.agg.txt'
  echo '               new.docked.agg.txt'
  echo ''
  echo '         Sufflix of aggregrated file: agg.txt'
  echo '         Old and New files must have mostly SAME NAME'
  echo ''
  exit
endif

set new_file = $argv[1]
set old_path = $argv[2]
set new_suff = $argv[3]
set old_suff = $argv[4]
set agg_suff = $argv[5]

foreach new_file (`cat $argv[1]`)

  set new_name = `basename $new_file .$new_suff`
  
  cat $old_path/$new_name.$old_suff $new_file |  \
  sed 's/Title/## Title/g' | sort -hk2 \
    > $new_name.$agg_suff

end
