import numpy as np

import matplotlib.pyplot as plt

# Load the data
date = "2025-02-11/"
prefix="data/"+date
data = np.genfromtxt(prefix+'viscosity_temperature_curve.csv', skip_header=1, delimiter=',', names=['Temperature', 'Viscosity'])

# Assuming the CSV has columns 'Temperature' and 'Viscosity'
temperature = data['Temperature']
viscosity = data['Viscosity']

dataArt = np.genfromtxt('thPoints.csv', skip_header=1, delimiter=',', names=['Temperature', 'Viscosity'])

# Assuming the CSV has columns 'Temperature' and 'Viscosity'
temperatureArt = dataArt['Temperature']
viscosityArt = dataArt['Viscosity']

# Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(temperature, viscosity*1e3, label='Nos valeurs :(', marker='o', color='b')
plt.plot(temperatureArt, viscosityArt, label='Valeurs de l\'article :)', marker='o', linestyle='-', color='r')
plt.title('Viscosité en fonction de la température')
plt.xlabel('Température (K)')
plt.ylabel('Viscosité (mPa.s)')
plt.grid(True)
plt.legend()
plt.show()