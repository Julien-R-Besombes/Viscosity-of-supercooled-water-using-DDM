import numpy as np
import matplotlib.pyplot as plt

# Load the data
date = "2025-02-18/"
prefix="data/"+date
data = np.genfromtxt(prefix+'viscosity_temperature_curve_512.csv', skip_header=1, delimiter=',', names=['Temperature', 'Viscosity'])
data2 = np.genfromtxt(prefix+'viscosity_temperature_curve_256.csv', skip_header=1, delimiter=',', names=['Temperature', 'Viscosity'])
# Assuming the CSV has columns 'Temperature' and 'Viscosity'
temperature = data['Temperature']
viscosity = data['Viscosity']
temperature2 = data2['Temperature']
viscosity2 = data2['Viscosity']

dataArt = np.genfromtxt('smoothed_values_viscosity_PNAS2015.csv', skip_header=1, delimiter=',', names=['Temperature', 'Viscosity'])

# Assuming the CSV has columns 'Temperature' and 'Viscosity'
temperatureArt = dataArt['Temperature']
viscosityArt = dataArt['Viscosity']

# Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(temperature, viscosity*1e3, label='Valeurs 02/18, 512px, non-corrigées, a non fixée', marker='+', color='g')
plt.scatter(temperature2, viscosity2*1e3, label='Valeurs 02/18, 256px, non-corrigées, a non fixée', marker='+', color='b')
plt.plot(temperatureArt, viscosityArt, label='Valeurs de l\'article :)', marker='+', linestyle='-', color='r')
plt.title('Viscosité en fonction de la température')
plt.xlabel('Température (K)')
plt.ylabel('Viscosité (mPa.s)')
plt.grid(True)
plt.legend()
plt.show()