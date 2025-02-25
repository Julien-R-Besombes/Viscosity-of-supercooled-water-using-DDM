import numpy as np
import csv

# Load the data
prefix = "data/2025-02-25/"
data = np.genfromtxt(prefix+'temperature.csv', skip_header=1, delimiter=',', names=['Index', 'Temperature'])
temperature_index = data['Index'].astype(int)
temperature = data['Temperature']

# Define the correction function
def correct_temperature(temp, a=0, b=4.5):
    return temp + a*temp + b

# Apply the math function to the temperature data
#a = -0.0819
#b = 22.73+4.5
# Define the variables
T0 = 0 + 273.15
T1 = -25.33 + 273.15
dT0 = T0 - (-0.9 + 273.15)
dT1 = T1 - (-28 + 273.15)

# Calculate a and b
a = (dT1 - dT0) / (T1 - T0)
b = dT0 - a * T0
corrected_temperature = [correct_temperature(temp, a, b) for temp in temperature]

# Write the corrected data to a new CSV file
output_file = prefix + 'corrected_temperature.csv'
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Index (i)', f'Corrected_Temperature (K) a = {a} b = {b}'])
    writer.writerows(zip(temperature_index, corrected_temperature))

