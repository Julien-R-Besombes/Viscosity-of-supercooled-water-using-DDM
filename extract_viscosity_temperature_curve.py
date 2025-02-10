import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import csv
import fastddm as fddm
from fastddm.fit import simple_structure_function, fit
from fastddm.azimuthalaverage import AAReader
import scipy.constants as c

def get_viscosity(filename, T, q_index = (35,130)):
    r = AAReader(filename)
    aa = r.load()
    q = aa.k
    time = aa.tau
    weights = 1/np.sqrt(time)

    # get tau(q) for each q
    tau = []
    for i in tqdm(range(*q_index)):
        result = fit(simple_structure_function, xdata=aa.tau, ydata=aa.data[i]/np.max(aa.data[i]), weights=weights)
        tau.append(result.best_values["tau"])

    x = q[q_index[0]:q_index[1]]
    y = tau
    y=np.array(y)
    x=np.array(x)

    # filter incoherent values
    x = x[y>1e-3]
    y = y[y>1e-3]

    # linear regression in log-log scale
    a, b = np.polyfit(np.log(x), np.log(y), 1)

    # get viscosity via Stokes-Einstein relation
    D = np.exp(-b)*1e-12 # m2/s
    a = 345e-9/2 # m
    eta = c.Boltzmann*T/(6*np.pi*D*a)

    return eta

def get_temperature(tempFilename):
    temperatures = {}
    with open(tempFilename+'.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            index = int(row[0])
            temp = float(row[1])
            temperatures[index] = temp
    return temperatures

def save_as_csv(temperatures, viscosities, filename):
    with open(filename+'.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['T (K)', 'eta (Pa.s)'])
        for temp, visc in zip(temperatures, viscosities):
            writer.writerow([temp, visc])

if __name__=="__main__":
    # Parameters
    date = "data/2025-02-04/"
    video_range = (19, 48)
    save_path = date+"extracted/"
    tempFilename = date+"temperature"
    q_index = (35,130)

    # Get temperatures
    temperatures = get_temperature(tempFilename)

    # Get viscosities
    viscosities = []
    for video in tqdm(range(*video_range)):
        filename = save_path+"resized"+str(video)+".aa.ddm"
        T = temperatures[video]
        eta = get_viscosity(filename, T, q_index)
        viscosities.append(eta)

    # Save as csv
    save_as_csv(temperatures, viscosities, date+"viscosity_temperature_curve")
    print("Done")
