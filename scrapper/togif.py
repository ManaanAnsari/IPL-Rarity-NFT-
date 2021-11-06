import glob
from PIL import Image
import os.path
from pathlib import Path

image_files_dir = './../ipl-imgs'
gif_files_dir = './../ipl-gifs'

def make_dir(dir_path):
    Path(dir_path).mkdir(parents=True, exist_ok=True)


for path, directories, files in os.walk(image_files_dir):
    # print(path,directories,files)
    if len(files) and len(directories) ==0:
        try:
            # we are inside images vala dir
            filenames = [ os.path.join(path, f) for f in files]
            print(path,filenames)
            # outputs
            out_path = path.split('/')
            gif_filename = out_path[-1].replace(" ","_")+".gif"
            out_path = '/'.join(out_path[:-1])
            out_path = out_path.replace(image_files_dir,gif_files_dir)
            make_dir(out_path)
            # break
            fp_out = os.path.join(out_path,gif_filename)
            print("output: ",fp_out)
            img, *imgs = [Image.open(f).resize((500,300), Image.ANTIALIAS) for f in sorted(filenames)]
            print(img)
            img.save(fp=fp_out, format='GIF', append_images=imgs,
                    save_all=True, duration=400, loop=0)
        except Exception as e:
            # to do handle later
            print(e)
