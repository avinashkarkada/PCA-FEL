import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc

# Set font to Times New Roman
rc('font', family='serif', serif='Times New Roman')

data = np.genfromtxt('2d_proj_ymg.xvg', skip_header=17)
x = data[:, 0]
y = data[:, 1]
colors = np.arange(1, len(y) + 1)

plt.scatter(x, y, marker='o', c=colors, cmap='viridis', label='Data Points')

# Set font for color bar label
cbar = plt.colorbar(label='Frames')
cbar.set_label('Frames', fontsize=12, fontweight='bold')  # Correct: cbar.set_label()

# Set font for title, xlabel, and ylabel
plt.title('YMG', fontsize=16, fontweight='bold')
plt.xlabel('PC1', fontsize=14, fontweight='bold')
plt.ylabel('PC2', fontsize=14, fontweight='bold')

# Set font for tick labels (corrected for compatibility)
plt.tick_params(axis='both', which='major', labelsize=12)  # Removed labelweight

# Adjust font weight and thickness for tick labels and axis spines
for label in plt.gca().get_xticklabels() + plt.gca().get_yticklabels():
    label.set_fontweight('bold')

for spine in plt.gca().spines.values():
    spine.set_linewidth(2)  # Increase axis thickness

# Save the plot with high quality
plt.savefig('PCA.eps', format='eps', bbox_inches='tight')
plt.savefig('PCA.png', format='png', dpi=1200, bbox_inches='tight')

plt.show()

