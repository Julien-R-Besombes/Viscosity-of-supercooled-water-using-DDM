import numpy as np
import matplotlib.pyplot as plt

# Load the data
date = "2025-02-18/"
prefix="data/"+date
data = np.genfromtxt(prefix+'viscosity_temperature_curve_512.csv', skip_header=1, delimiter=',', names=['Temperature', 'Viscosity'])
#data2 = np.genfromtxt(prefix+'viscosity_temperature_curve_256.csv', skip_header=1, delimiter=',', names=['Temperature', 'Viscosity'])
# Assuming the CSV has columns 'Temperature' and 'Viscosity'
temperature = data['Temperature']
viscosity = data['Viscosity']
#temperature2 = data2['Temperature']
#viscosity2 = data2['Viscosity']

dataArt = np.genfromtxt('smoothed_values_viscosity_PNAS2015.csv', skip_header=1, delimiter=',', names=['Temperature', 'Viscosity'])

# Assuming the CSV has columns 'Temperature' and 'Viscosity'
temperatureArt = dataArt['Temperature']
viscosityArt = dataArt['Viscosity']

# Plot the data
fig, ax1 = plt.subplots(figsize=(10, 6))

# Primary x-axis (Temperature in K)
ax1.scatter(temperature, viscosity*1e3, label='Valeurs 02/18, 512px, non-corrigées, a non fixée', marker='+', color='g')
#ax1.scatter(temperature2, viscosity2*1e3, label='Valeurs 02/18, 256px, non-corrigées, a non fixée', marker='+', color='b')
ax1.plot(temperatureArt, viscosityArt, label='Smoothed values (PNAS 2015)', marker='+', linestyle='-', color='r')
ax1.set_xlabel('Température (K)')
ax1.set_ylabel('Viscosité (mPa.s)')
ax1.grid(True)

# Secondary x-axis (Temperature in °C)
ax2 = ax1.twiny()
ax2.set_xlim(ax1.get_xlim())
ax2.set_xticks(ax1.get_xticks())
ax2.set_xticklabels([f'{x-273.15:.1f}' for x in ax1.get_xticks()])
ax2.set_xlabel('Température (°C)')

# Add title and legend
fig.suptitle('Viscosité en fonction de la température')
ax1.legend()

plt.show()