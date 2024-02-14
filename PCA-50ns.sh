/usr/local/gromacs-2019/bin/gmx covar -f Protein1.pdb -s Protein1.tpr -o eigenval.xvg -v eigenvect.trr -xpm covara.xpm
/usr/local/gromacs-2019/bin/gmx xpm2ps -f covara.xpm -o covara.eps -do covar.m2p
/usr/local/gromacs-2019/bin/gmx anaeig -v eigenvect.trr -f Protein1.pdb -s Protein1.tpr -first 1 -last 2 -proj proj_eig.xvg -2d 2d_proj.xvg
/usr/local/gromacs-2019/bin/gmx sham -f 2d_proj.xvg -ls gibbs.xpm -notime
/usr/local/gromacs-2019/bin/gmx xpm2ps -f gibbs.xpm  -o gibbs.eps -rainbow blue 
