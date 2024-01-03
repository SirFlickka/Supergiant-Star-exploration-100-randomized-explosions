import numpy as np
import matplotlib.pyplot as plt

# Constants for the simulation
num_elements = 100  # Number of elements in the accretion disk
num_energy_bins = 50  # Number of energy bins for the spectral map

# Define a list of potential elements
elements = ['H', 'He', 'C', 'O', 'Ne', 'Mg', 'Si', 'S', 'Fe']

# Create spectral maps for two neutron stars
spectral_maps = []
for _ in range(2):
    element_composition = np.random.choice(elements, num_elements)
    element_energy_bins = np.random.uniform(1, 30, num_elements)
    
    spectral_map = np.zeros((len(elements), num_energy_bins))
    
    for i, element in enumerate(elements):
        for j in range(num_energy_bins):
            spectral_map[i, j] = np.random.uniform(0.1, 1.0)
    
    spectral_maps.append((element_composition, element_energy_bins, spectral_map))

# Compare and plot spectral maps
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Neutron Star Spectral Maps Comparison')

for i, (composition, energy_bins, spectral_map) in enumerate(spectral_maps):
    row = i // 2
    col = i % 2
    
    axs[row, col].imshow(spectral_map, cmap='viridis', extent=[0, num_energy_bins, 0, len(elements)], aspect='auto')
    axs[row, col].set_title(f'Neutron Star {i + 1}')
    axs[row, col].set_xlabel('Energy Bins')
    axs[row, col].set_ylabel('Element')
    axs[row, col].set_yticks(np.arange(len(elements)))
    axs[row, col].set_yticklabels(elements)
    
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()
