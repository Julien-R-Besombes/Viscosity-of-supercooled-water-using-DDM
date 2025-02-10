import numpy as np

import matplotlib.pyplot as plt

# Load the data
date = "2025-02-04/"
prefix="data/"+date
data = np.genfromtxt(prefix+'viscosity_temperature_curve.csv', skip_header=1, delimiter=',', names=['Temperature', 'Viscosity'])

# Assuming the CSV has columns 'Temperature' and 'Viscosity'
temperature = data['Temperature']
viscosity = data['Viscosity']

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(temperature, viscosity*1e3, marker='o', linestyle='-', color='b')
plt.title('Viscosity vs Temperature')
plt.xlabel('Temperature (K)')
plt.ylabel('Viscosity (mPa.s)')
plt.grid(True)
plt.show()