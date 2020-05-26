import sys
import os
from PIL import Image, ImageFilter

# take the arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# check whether the file exists or create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# loop through every image in folder and convert them into png.
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    img.save(f'{output_folder}{filename}.png','png')
    print('all done')

