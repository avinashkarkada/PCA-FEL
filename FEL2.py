import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

data_file = 'your_data_file.txt'

data = np.loadtxt(data_file)

pc1 = data[:, 0]
pc2 = data[:, 1]
genergy = data[:, 2]

grid_size = int(np.sqrt(len(genergy)))
genergy_surface = genergy.reshape((grid_size, grid_size))

rc('font', family='serif', serif='Times New Roman')

contour = plt.contourf(pc1.reshape((grid_size, grid_size)), pc2.reshape((grid_size, grid_size)), genergy_surface, cmap='inferno')
#[viridis, plasma, inferno, magma, cividis, coolwarm, cubehelix, spring, summer, autumn, winter, RdYlBu, rainbow]
colorbar = plt.colorbar(contour, label='Gibbs Free Energy (kJ/mol)')

cbar_label = colorbar.ax.yaxis.label
cbar_label.set_fontsize(12)
cbar_label.set_fontweight('bold')

for tick in colorbar.ax.yaxis.get_ticklabels():
    tick.set_fontsize(10)
    tick.set_fontweight('bold')


plt.xlabel('PC1', fontsize=14, fontweight='bold')
plt.ylabel('PC2', fontsize=14, fontweight='bold')

plt.gca().spines['top'].set_linewidth(2)
plt.gca().spines['right'].set_linewidth(2)
plt.gca().spines['bottom'].set_linewidth(2)
plt.gca().spines['left'].set_linewidth(2)

plt.tick_params(axis='both', which='major', width=2, length=6, labelsize=12)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

plt.title('FEL', fontsize=16, fontweight='bold')

plt.savefig('free_energy_landscape.png', dpi=800, bbox_inches='tight')


plt.show()

