import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter, FuncAnimation


video = 46
date="data/2025-02-04/"
prefixe = date+"video"+str(video)+"/Video"+str(video)+"image"
N = 500
images = []
imDiff = []


for i in tqdm(range(N)):
    images.append(plt.imread(prefixe+str(i)+".bmp"))

imDiff = np.abs(images - images[0])

plt.subplot(1,3,1)
plt.title(r"Différence à $\Delta t = \delta t$")
plt.imshow(imDiff[1], cmap='gray')
plt.subplot(1,3,2)
plt.title(r"Différence à $\Delta t = 10 \delta t$")
plt.imshow(imDiff[10], cmap='gray')
plt.subplot(1,3,3)
plt.title(r"Différence à $\Delta t = 499 \delta t$")
plt.imshow(imDiff[499], cmap='gray')
plt.show()

fig, ax = plt.subplots()

def update(frame):
    ax.imshow(imDiff[frame])
    ax.set_title("Différence à $\Delta t$ = "+str(frame)+" $\delta t$, défilement x2")

ani = animation.FuncAnimation(fig, update, frames=N, interval=5, repeat=False) 
plt.show()
plt.close(fig)
writer = PillowWriter(fps=200)
ani.save('ani.gif', writer=writer)
