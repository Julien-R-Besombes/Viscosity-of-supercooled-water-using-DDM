import fastddm as fddm

video = 5
date = "data/2025-02-04/"
prefixe = date+"/video"+str(video)+"/Video"+str(video)+"image"
N = 500

#DDM
file_names = [prefixe+str(i)+".bmp" for i in range(N)]
images = fddm.read_images(file_names)
pixel_size = 265.5e-3    # um
frame_rate = 100    # frames per second

# compute image structure function and set experimental parameters
dqt = fddm.ddm(images, range(1, len(images)))
dqt.pixel_size = pixel_size
dqt.set_frame_rate(frame_rate)

# compute the azimuthal average
aa = fddm.azimuthal_average(dqt, bins=dqt.shape[-1] - 1, range=(0.0, dqt.ky[-1]))
aa.save(date+"extracted/aa"+str(video))
