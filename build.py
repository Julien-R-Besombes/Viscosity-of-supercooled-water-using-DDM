import fastddm as fddm
from tqdm import tqdm
from fastddm.fit import simple_structure_function, fit
import os

def buildDDMFile(prefix, save_path, N=500, px_size=265e-3, fps=100):
    """
        Build .ddm file based on one video. Images must be stored s.a. [prefix][i].bmp is the direction (for image n°i).
        prefix: prefix (str)
        N: number of images (int ; optionnal, 500 by default)
        px_size: pixel size um (float ; optionnal, 265e-3 by default)
        fps: frame rate in fps/Hz (float ; optionnal, 100 by default)
    """
    #DDM
    file_names = [prefix+str(i)+".bmp" for i in range(N)]
    images = fddm.read_images(file_names)

    # compute image structure function and set experimental parameters
    dqt = fddm.ddm(images, range(1, len(images)))
    dqt.pixel_size = px_size
    dqt.set_frame_rate(fps)

    # compute the azimuthal average
    aa = fddm.azimuthal_average(dqt, bins=dqt.shape[-1] - 1, range=(0.0, dqt.ky[-1]))

    # save it 
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    aa.save(save_path+"resized"+str(video))

if __name__=="__main__":
    date = "data/2025-02-04/"
    video_range = (1, 48)
    save_path = date+"extracted/"
    for video in tqdm(range(*video_range)):
        prefix = date+"/video"+str(video)+"/video"+str(video)+"_resized/Video"+str(video)+"image"
        buildDDMFile(prefix, save_path=save_path)


