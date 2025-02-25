import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from fastddm.fit import simple_structure_function, fit
from fastddm.azimuthalaverage import AAReader
from scipy.optimize import curve_fit
import scipy.constants as c

a = []
b = []
b2 = []

def f(x, b2):
    return np.exp(-2*np.log(x) + b2)

for k in tqdm(range(1,11)):
    video = k
    date = "data/2025-02-18/"
    filename = date+"extracted/resized_size512_"+ str(video)+".aa.ddm"
    
    r = AAReader(filename)
    aa = r.load()
    q = aa.k
    time = aa.tau
    weights = 1/np.sqrt(aa.tau)
    simple_structure_function.set_param_hint("B", min=-np.inf, max=np.inf, value=0.0)

    q_index = [30,100]
    tau = []
    for i in range(q_index[0], q_index[1]):
        result = fit(simple_structure_function, xdata=aa.tau, ydata=aa.data[i]/np.max(aa.data[i]), weights=weights)
        tau.append(result.best_values["tau"])
        
    x = q[q_index[0]:q_index[1]]
    y = tau
    x_th = np.linspace(np.min(x), np.max(x), 100)
    y = np.array(y)
    x = np.array(x)
    x = x[y>1e-3]
    y=y[y>1e-3]
    a.append(np.polyfit(np.log(x), np.log(y), 1)[0])
    b.append(np.polyfit(np.log(x), np.log(y), 1)[1])
    
    popt, pcov = curve_fit(f, x, y)
    b2.append(popt[0])


b = np.array(b)
b2 = np.array(b2)

a_std, b_std, b2_std = np.std(a), np.std(b), np.std(b2)
a_mean, b_mean, b2_mean= np.mean(a), np.mean(b), np.mean(b2)
plt.xscale("log")
plt.yscale("log")
plt.scatter(x, y)
plt.xlabel(r"$q (\mu m)^{-1}$")
plt.ylabel(r"$\tau (s)$")
plt.plot(x_th, np.exp(a_mean*np.log(x_th) + b_mean), label=fr"Modèle $ax+b$, a = {a_mean:.4f} ± {a_std:.4f}, b = {b_mean:.4f} ± {b_std:.4f}")
plt.plot(x,f(x, b2_mean), label=f"Modèle $ax+b$ avec a=-2 et b={popt[0]:.4f} ± {b2_std:.4f}")
plt.legend()
plt.show()

abscisse = np.arange(1,len(a)+1,1)
plt.scatter(abscisse,a)
plt.plot(abscisse, [a_mean]*len(a), label=f'a moyen={a_mean:.4f},std={a_std:.4f}')
plt.ylabel("a")
plt.legend()
plt.show()

plt.scatter(abscisse,b)
plt.plot(abscisse, [b_mean]*len(a), label=f'b moyen={b_mean:.4f},std={b_std:.4f}')
plt.ylabel("b")
plt.legend()
plt.show()

plt.scatter(abscisse,b2)
plt.plot(abscisse, [b2_mean]*len(a), label=f'b2 moyen={b2_mean:.4f},std={b2_std:.4f}')
plt.ylabel("b2")
plt.legend()
plt.show()

D1 = np.array(np.exp((-1)*b)*1e-12) # en m²/s  
T = 273.15 + 20
r = (345e-9)/2
eta1 = c.Boltzmann*T/(6*np.pi*D1*r)
eta1_mean,eta1_std=np.mean(eta1),np.std(eta1)

plt.scatter(abscisse,eta1)
plt.plot(abscisse, [eta1_mean]*len(a), label=f"eta moyen = {eta1_mean:.6f} (à 20 degrés) en ne fixant pas a, std={eta1_std:.6f}")
plt.ylabel("eta1")
plt.legend()
plt.show()

D2 = np.array(np.exp((-1)*b2)*1e-12) # en m²/s  
eta2 = c.Boltzmann*T/(6*np.pi*D2*r)
eta2_mean, eta2_std = np.mean(eta2), np.std(eta2)

plt.scatter(abscisse,eta2)
plt.plot(abscisse, [eta2_mean]*len(a), label=f'eta moyen= {eta2_mean:.6f} (à 20 degrés) en fixant a=-2,std={eta2_std:.6f}')
plt.ylabel("eta2")
plt.legend()
plt.show()