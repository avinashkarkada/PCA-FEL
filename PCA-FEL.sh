#!/bin/bash

echo "Enter Protein'_'"
read n
declare -i num=$n+0

printf "%s\n" "4" "4" | gmx covar -f ../step5_production*.xtc -s Protein$num.tpr -o eigenval.xvg -v eigenvect.trr -xpm covara.xpm
gmx xpm2ps -f covara.xpm -o covara.eps -do covar.m2p
printf "%s\n" "4" "4" | gmx anaeig -v eigenvect.trr -f ../step5_production*.xtc -s Protein$num.tpr -first 1 -last 2 -proj proj_eig.xvg -2d Protein$num_2d_proj.xvg
gmx sham -f Protein$num_2d_proj.xvg -ls gibbs.xpm -notime
gmx xpm2ps -f gibbs.xpm  -o gibbs.eps -rainbow blue 

python2.7 xpm2txt.py -f gibbs.xpm -o Protein0_gibbs.txt
python3 FEL.py
