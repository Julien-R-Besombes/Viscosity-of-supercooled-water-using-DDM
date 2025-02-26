import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

video = 22
date="data/2025-02-04/"
prefixe = date+"video"+str(video)+"/video"+str(video)+"_resized/Video"+str(video)+"image"
N = 500
images = []
imDiff = []

for i in tqdm(range(N)):
    images.append(plt.imread(prefixe+str(i)+".bmp"))

imDiff = np.abs(images - images[0])

fig, ax = plt.subplots()

def update(frame):
    ax.imshow(imDiff[frame])
    ax.set_title("Différence à $\Delta t$ = "+str(frame)+" $\delta t$, défilement x2")

ani = animation.FuncAnimation(fig, update, frames=N, interval=5, repeat=False) 
plt.show()
plt.close(fig)
writer = PillowWriter(fps=200)
ani.save('ani.gif', writer=writer)
