import os
from PIL import Image
from tqdm import tqdm

def resize_image(image_path, output_path, size=(512, 512)):
    with Image.open(image_path) as img:
        width, height = img.size
        new_width, new_height = size
        left = (width - new_width) / 2
        top = (height - new_height) / 2
        right = (width + new_width) / 2
        bottom = (height + new_height) / 2
        img = img.crop((left, top, right, bottom))
        img = img.resize(size, Image.LANCZOS)
        img.save(output_path)

def process_folder(folder_name):
    input_folder = os.path.join(os.getcwd(), folder_name)
    for subfolder in tqdm(os.listdir(input_folder)):
        subfolder_path = os.path.join(input_folder, subfolder)
        if os.path.isdir(subfolder_path):
            output_subfolder = os.path.join(subfolder_path, f"{subfolder}_resized")
            os.makedirs(output_subfolder, exist_ok=True)

            for filename in tqdm(os.listdir(subfolder_path)):
                if filename.lower().endswith('.bmp'):
                    input_path = os.path.join(subfolder_path, filename)
                    output_path = os.path.join(output_subfolder, filename)
                    resize_image(input_path, output_path)

if __name__ == "__main__":
    folders = ['data/2025-01-28', 'data/2025-02-04']
    for folder in tqdm(folders):
        process_folder(folder)