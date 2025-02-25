import numpy as np
import csv

# Load the data
prefix = "data/2025-02-18/"
data = np.genfromtxt(prefix+'temperature.csv', skip_header=1, delimiter=',', names=['Index', 'Temperature'])
temperature_index = data['Index'].astype(int)
temperature = data['Temperature']

# Define the correction function
def correct_temperature(temp):
    return temp + 4.5

# Apply the math function to the temperature data
corrected_temperature = [correct_temperature(temp) for temp in temperature]

# Write the corrected data to a new CSV file
output_file = prefix + 'corrected_temperature.csv'
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Index (i)', 'Corrected_Temperature (K)'])
    writer.writerows(zip(temperature_index, corrected_temperature))

