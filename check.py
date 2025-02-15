import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


video = 22
date="data/2025-02-04/"
prefixe = date+"video"+str(video)+"/video"+str(video)+"_resized/Video"+str(video)+"image"
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