import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(0)

# Generate random data for 100 supergiant collapses
num_collapses = 100
data = {
    'Supergiant ID': range(1, num_collapses + 1),
    'Surface Composition': np.random.choice(['H', 'He'], num_collapses),
    'Result': np.random.choice(['Larger Supergiant', 'Accretion Disk', 'Neutron Star', 'Nothing'], num_collapses)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Filter for supergiants that are 7-9x larger
larger_supergiants = df[(df['Result'] == 'Larger Supergiant')]

# Display the DataFrame
print("All Supergiant Collapses:")
print(df)

print("\nSupergiants 7-9x Larger:")
print(larger_supergiants)
