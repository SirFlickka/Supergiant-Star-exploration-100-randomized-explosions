import numpy as np
import matplotlib.pyplot as plt

# Constants for the simulation
num_elements = 1000  # Number of elements in the accretion disk
element_masses = np.random.uniform(1, 30, num_elements)  # Masses of elements (simplified)
element_composition = np.random.choice(['H', 'He', 'C', 'O', 'Fe'], num_elements)  # Simplified element composition
element_temperature = np.random.uniform(1000, 10000, num_elements)  # Temperature of elements (simplified)
element_radius = np.random.uniform(1e3, 1e5, num_elements)  # Radius of elements (simplified)

# Calculate element luminosity (simplified)
element_luminosity = (element_masses / element_radius**2) * element_temperature**4

# Create a DataFrame (requires pandas)
import pandas as pd

data = pd.DataFrame({
    'Element Mass (M_sun)': element_masses,
    'Element Composition': element_composition,
    'Element Temperature (K)': element_temperature,
    'Element Radius (km)': element_radius,
    'Element Luminosity (L_sun)': element_luminosity
})

# Display the DataFrame
print(data.head())

# Plot element luminosity vs. temperature
plt.figure(figsize=(8, 4))
plt.scatter(data['Element Temperature (K)'], data['Element Luminosity (L_sun)'], c='b', alpha=0.5)
plt.xlabel('Element Temperature (K)')
plt.ylabel('Element Luminosity (L_sun)')
plt.title('Neutron Star Accretion Disk Element Luminosity vs. Temperature')
plt.grid(True)
plt.show()
