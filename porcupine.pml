load ev1.pdb
#make sure the python script is in the current directory.
run modevectors.py
split_states ev1
modevectors ev1_0001, ev1_0050, cutoff=.0, head_length=2, head=0.4, headrgb=(1,.2,.1) ,tailrgb=(1,.2,.1) ,notail=0
set cartoon_trace,1
set cartoon_tube_radius, 0.3
cmd.disable('all')
cmd.enable('ev1_0001',1)
cmd.enable('modevectors',1)
set ray_shadow,0

#save PCA_porcupine_ev1.pse,format=pse
