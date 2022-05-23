import numpy as np 
from PIL import Image

im_gray = np.array(Image.open('FILE DIRECTORY PATH').convert('L'))
print(type(im_gray))

thresh = 128

im_bool = im_gray > thresh
print(im_bool)


maxval = 255

im_bin = (im_gray > thresh) * maxval


Image.fromarray(np.uint8(im_bin)).save('DIRECTORY WE WANT TO SAVE NEW IMAGE TOO')

im_bin_keep = (im_gray > thresh) * im_gray
print(im_bin_keep)


Image.fromarray(np.uint8(im_bin_keep)).save('DIRECTORY WE WANT TO SAVE NEW IMAGE TOO')