#!/bin/csh

##
##	Peter M.U. Ung	@ MSSM
##	16.05.13 -- updated
##
##  This is a special case
##  Only use when combining 2 sets of docking on the same receptor
##  to calculate teh aggregate AUC result
##
##	Use it to do a batched AUC figure generation
##	Use after data are aggregated with run_aggregate_auc.csh
##

if ($#argv != 4) then
  echo ''
  echo '    Usage: x.csh '
  echo '                 [ list of files for AUC ]'
  echo '                 [ Active file ]'
  echo '                 [ sufflix to remove ]'
  echo '                 [ new sufflix for output ]'
  echo ''
  echo '    e.g.> x.csh  agg.list  ../tight.list  docked.agg.txt  agg.tig'
  echo ''
  exit
endif

set file   = $argv[1]
set active = $argv[2]
set remove = $argv[3]
set addon  = $argv[4]

foreach txt (`cat $file`)

  set name = `basename $txt .$remove`
  ./1_job_AUC.csh      \
    $txt               \
    $active            \
    $name.$addon
end
