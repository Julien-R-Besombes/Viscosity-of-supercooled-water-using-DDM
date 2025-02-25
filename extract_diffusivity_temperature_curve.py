import numpy as np
import csv
from fastddm.fit import simple_structure_function, fit
from fastddm.azimuthalaverage import AAReader
from extract_viscosity_temperature_curve import get_temperature

def get_diffusivity(filename, q_index=(15, 62)):
    r = AAReader(filename)
    aa = r.load()
    q = aa.k
    time = aa.tau
    weights = 1/np.sqrt(time)
    simple_structure_function.set_param_hint("B", min=-np.inf, max=np.inf, value=0.0)
    # get tau(q) for each q
    tau = []
    for i in range(*q_index):
        result = fit(simple_structure_function, xdata=aa.tau, ydata=aa.data[i]/np.max(aa.data[i]), weights=weights)
        tau.append(result.best_values["tau"])

    x = q[q_index[0]:q_index[1]]
    y = tau
    y = np.array(y)
    x = np.array(x)

    # filter incoherent values
    x = x[y > 1e-3]
    y = y[y > 1e-3]

    # linear regression in log-log scale
    a1, b = np.polyfit(np.log(x), np.log(y), 1)

    # get diffusivity
    D = np.exp(-b) * 1e-12  # m2/s
    
    print(f"Video {filename} a: {a1} b: {b} Diffusivity: {D:.2e} m^2/s")

    return D


def save_as_csv(temperatures, diffusivities, filename):
    with open(filename+'.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['T (K)', 'D (m^2/s)'])
        for temp, diff in zip(temperatures, diffusivities):
            writer.writerow([temp, diff])

if __name__ == "__main__":
    # Parameters
    date = "data/2025-02-18/"
    video_range = (1, 29)
    save_path = date + "extracted/"
    tempFilename = date + "corrected_temperature"
    q_index = (30, 100)

    # Get temperatures
    temperatures = get_temperature(tempFilename)

    # Get diffusivities
    diffusivities = []
    for video in range(*video_range):
        filename = save_path + "resized_size512_" + str(video) + ".aa.ddm"
        D = get_diffusivity(filename, q_index)
        diffusivities.append(D)

    # Save as csv
    temp = [temperatures[i] for i in range(*video_range)]
    save_as_csv(temp, diffusivities, date + "corrected_diffusivity_temperature_curve_512")
    print("Done")