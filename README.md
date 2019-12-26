# Ligand_Enrichment
Calculate the AUC performance of Virtual Screening Enrichment

The general process is:
- Create a file only with the names of the ligands in the dataset ranked by the score (like in the Examples directoy)
- Create a file actives.txt only with the names of the known substrates
- run 1_calc_AUC.csh to get the enrichment profiles (enr.dud, enr1000.dud) and the AUC graphs

##########################################################################

```
> 1_calc_AUC.csh
      [ Ranked Data File: .txt ] # use 1st col; no header
      [ Known Actives:    .txt ] # use 1st col; no header
      [ AUC Output Prefix      ]
      [ figure format: png|svg ]
      [ Directory of Script    ]

  e.g.> *.csh  ranked_data.txt  known_actives.txt  
               performance_auc  svg
               "/directory/to/enrich_scripts"
```
- This shell script is a wrapper for a set of python scripts to calculate the enrichment factor and AUC/logAUC value of binding result of known ligands from a set of known nonbinders. Supply a ranked result file and a known binders file to calculate AUC.

- The result is a figure with both AUC and log(AUC) plots with the performance value labeled in it. Any figure format **Matplotlib** can handle can be used: jpg, png, svg, eps, ps, pdf, etc. _SVG_ offers more compactness.
![auc plot](https://github.com/mungpeter/Ligand_Enrichment/blob/master/Examples/performance_auc.AUC.svg)

```
> 2_batch_AUC.csh
      [ List of Ranked Data Files: .txt ]
      [ Known Actives:             .txt ]
      [ Figure format:          png|svg ]
      [ Directory of Script             ]

  e.g.> *.csh  score.list  known_actives.txt  svg
               "/directory/to/enrich_scripts"
```
- This batch-mode shell script basically loops **1_job_AUC.csh** over a list of ranked data files. supply a list of ranked docking result files and a known binders file to calculate AUC for each individual docking result on the list.


#############################
- For a very special case where 2 docking results on the same receptor need to be combined before calculating hte AUC values:

```
> run_aggregate_auc_step1.csh
> run_aggregate_auc_step2.csh
```

##########################################################################
# Required Packages
```
csh/tcsh       # shell
perl           #
python         # 3.6.8+
   numpy       # 1.16.2+
   pandas      # 0.24.2+
   matplotlib  # 3.0.3+
```