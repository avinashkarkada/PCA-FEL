#!/usr/bin/env python3

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
from matplotlib import cm
from scipy.interpolate import griddata
from scipy.interpolate import Rbf
from numpy import linspace
import matplotlib
from scipy import interpolate
import matplotlib.mlab as ml




##############3D#################################################################################################################
fig = plt.figure(figsize=None, dpi=300, facecolor=None, edgecolor=None, linewidth=0.0, frameon=None, subplotpars=None, tight_layout=None)
ax = fig.add_subplot(111, projection='3d')

### input file with x,y,z coordinates
x,y,z = np.loadtxt('Protein0_gibbs.txt').T
X,Y = np.unique(x),np.unique(y)
xi = linspace(min(X),max(X),len(X))
yi = linspace(min(Y),max(Y),len(Y))
xi,yi = np.meshgrid(xi,yi)
X1, Y1 = np.meshgrid(X,Y)

print (len(x))

Z = griddata((x,y),z,(X1,Y1),method='cubic')
surf = ax.plot_surface(X1, Y1, Z, rstride=1,cstride=1,alpha=1,cmap=cm.jet, linewidth=0.0, antialiased=3)
cset = ax.contourf(X1, Y1, Z, zdir='z', offset=-0, cmap=cm.jet, antialiased=3, vmin=0, vmax=18)

### put name of each axis. Cgange fontsize and lablesize accordingly
ax.set_xlabel('PC1',fontsize=12)
#ax.set_xlim(-6, 6)
ax.tick_params(axis="x", labelsize=6)
ax.set_ylabel('PC2',fontsize=12)
#ax.set_ylim(-6, 6)
ax.tick_params(axis="y", labelsize=6)
#ax.set_zlabel('Z axis', fontsize=12)
ax.tick_params(axis="z", labelsize=6)
ax.set_zlim(0, 18)

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.8, aspect=20)
#fig.colorbar(surf, shrink=0.8, aspect=20, extend='neither', ticks=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
fig.colorbar(cset, shrink=0.8, aspect=20, extend='neither', ticks=range(0, 21, 2))
#fig.colorbar(surf, shrink=0.8, aspect=20, ticks=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
#fig.clim(0.0,20.0)

plt.savefig('0_3D-FEL.jpg', dpi=300)





###############2D##########################################################################################################################
# create unique x and y values
X,Y = np.unique(x),np.unique(y)

# create a meshgrid of x and y values
xi = linspace(min(X),max(X),len(X))
yi = linspace(min(Y),max(Y),len(Y))
xi,yi = np.meshgrid(xi,yi)

# create another meshgrid of x and y values
X1, Y1 = np.meshgrid(X,Y)

# interpolate z values at the given x and y coordinates
Z = griddata((x,y),z,(X1,Y1),method='cubic')

# create a figure and axis object
fig = plt.figure(figsize=None, dpi=300)
ax = fig.add_subplot(111)

# create a contour plot
cset = ax.contourf(X1, Y1, Z, zdir='z', offset=-0, cmap=cm.jet, antialiased=3, vmin=0, vmax=18)

# set x and y labels
ax.set_xlabel('PC1',fontsize=12)
ax.tick_params(axis="x", labelsize=6)
ax.set_ylabel('PC2',fontsize=12)
ax.tick_params(axis="y", labelsize=6)

# Save plot to file
plt.savefig('0_2D-FEL.jpg', dpi=300)




