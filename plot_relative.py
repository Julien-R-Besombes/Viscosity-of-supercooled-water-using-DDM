import numpy as np
import matplotlib.pyplot as plt

# Load the data
date = "2025-02-25/"
prefix="data/"+date
data = np.genfromtxt(prefix+'corrected_diffusivity_temperature_curve_512.csv', skip_header=1, delimiter=',', names=['Temperature', 'diffusivity'])
temperature = data['Temperature']
diffusivity = data['diffusivity']
data_raw = np.genfromtxt(prefix+'diffusivity_temperature_curve_512.csv', skip_header=1, delimiter=',', names=['Temperature', 'diffusivity'])
temperature_raw = data_raw['Temperature']
diffusivity_raw = data_raw['diffusivity']

# Load the data from the article
dataArt = np.genfromtxt('smoothed_values_viscosity_PNAS2015.csv', skip_header=1, delimiter=',', names=['Temperature', 'Viscosity'])
temperatureArt = dataArt['Temperature']
viscosityArt = dataArt['Viscosity']

# Compute viscosity from diffusivity
D0 = 1.22 * 1e-12 # m²/s 1.22 => 02/25 ; th : 1.086
eta0 = 1.0016 * 1e-3 # Pa.s
T0 = 273.15 + 20
viscosity = eta0*(D0/diffusivity)*(temperature/T0)
viscosity_raw = eta0*(D0/diffusivity_raw)*(temperature_raw/T0)

# Plot the data
fig, ax1 = plt.subplots(figsize=(10, 6))

# Primary x-axis (Temperature in K)
ax1.scatter(temperature, viscosity*1e3, label='Valeurs 02/25, 512px, corrigées, a non fixée', marker='+', color='g')
ax1.scatter(temperature_raw, viscosity_raw*1e3, label='Valeurs 02/25, 512px, non corrigées, a non fixée', marker='+', color='b')
ax1.plot(temperatureArt, viscosityArt, label='Smoothed values (PNAS 2015)', marker='+', linestyle='-', color='r')
ax1.set_xlabel('Température (K)')
ax1.set_ylabel('Viscosité (mPa.s)')
ax1.set_title('Viscosité en fonction de la température')
ax1.grid(True)
ax1.legend()

# Secondary x-axis (Temperature in °C)
ax2 = ax1.twiny()
ax2.set_xlim(ax1.get_xlim())
ax2.set_xticks(ax1.get_xticks())
ax2.set_xticklabels([f'{int(t - 273.15)}' for t in ax1.get_xticks()])
ax2.set_xlabel('Température (°C)')

plt.show()
