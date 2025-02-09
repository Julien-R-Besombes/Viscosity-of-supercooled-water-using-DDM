import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from fastddm.fit import simple_structure_function, fit
from fastddm.azimuthalaverage import AAReader


video = 5
date = "data/2025-02-04/"
filename = date+"extracted/aa"+str(video)+".aa.ddm"

r = AAReader(filename)
aa = r.load()
q = aa.k
time = aa.tau

test_k = np.array([3, 5, 6, 7, 15], dtype=np.int64) * 2
for tk in test_k:    
    plt.scatter(time, aa.data[tk], marker="o", s=3, label="$q={:.3f}\ [\mu m^{{-1}}]$".format(q[tk]))
plt.xscale('log')
plt.yscale('log')
plt.xlabel("$\Delta t\ [s]$")
plt.ylabel(r"$|\Delta I(q,\Delta t)|^2$")
plt.title("Fonction de décorrélation")
plt.legend()
plt.show()

simple_structure_function.set_param_hint("B", min=-np.inf, max=np.inf, value=0.0)
colors = ["tab:" + col for col in ["blue", "orange", "green", "red"]]
fit_time = np.logspace(-2, 1.1)
labelstr = r"$A = {A:.2f},\ B = {B:.2f},\ \tau = {tau:.2f}s$"
weights = 1/np.sqrt(aa.tau)

fig = plt.figure(figsize=(9, 6))
for tk, color in zip(test_k, colors):    
    # fit for the given fixed index/k
    result = fit(simple_structure_function, xdata=aa.tau, ydata=aa.data[tk], weights=weights)
    
    # plot original data
    plt.scatter(aa.tau, aa.data[tk], marker="o", s=6, color=color, 
                label="$q={:.3f}\ [\mu m^{{-1}}]$".format(q[tk]))
    
    # and the fit
    plt.plot(fit_time, simple_structure_function.eval(**result.best_values, dt=fit_time), 
             color=color, linestyle="--", linewidth=0.8, label=labelstr.format(**result.best_values))

plt.xlabel("$\Delta t\ [s]$")
plt.ylabel("Fonction de décorrélation")
plt.title("Fonction de décorrélation fittée")
plt.legend()
plt.show()

tau = []
for i in tqdm(range(len(aa.data))):
    result = fit(simple_structure_function, xdata=aa.tau, ydata=aa.data[i], weights=weights)
    tau.append(result.best_values["tau"])

x = q[1:]
y = tau[1:]
x_th = np.linspace(np.min(x), np.max(x), 100)
plt.xscale("log")
plt.yscale("log")
plt.plot(x, y)
plt.xlim(1, 10)
plt.xlabel(r"$q \mu m$")
plt.ylabel(r"$\tau (s)$")
plt.plot(q, 1/q**2)
a, b = np.polyfit(np.log(x), np.log(y), 1)
plt.plot(x_th, np.exp(a*np.log(x_th) + b), label=f"Modèle $ax+b$ a = {a} et b = {b}")
plt.grid("b")
plt.legend()
plt.show()
