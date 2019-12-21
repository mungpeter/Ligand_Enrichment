#!/bin/csh

if ($#argv < 1) then
  echo ''
  echo '    Usage: x.csh [list of oeb.gz]'
  echo ''
  exit
endif

set cpu  = 12

foreach oeb (`cat $argv[1]`)
  set name = `basename $oeb .mod.oeb.gz`
  echo " ## Running on $name"

#  timeout  3h  \
  oempirun -np $cpu \
    fred -receptor /home/pmung/xxx_data/1_kinase/4_dyrk1a/0_oeb/$oeb \
         -dbase    /home/pmung/xxx_data/1_kinase/4_dyrk1a/3_sar/4_hit4/hit4.pka.oeb.gz \
         -prefix   $name \
#         -hitlist_size 0 \
#         -save_component_scores true \
         -docked_molecule_file $name.fred_docked.sdf \
         -score_file $name.fred_docked.txt

  echo "  ## Done with $name"
end
