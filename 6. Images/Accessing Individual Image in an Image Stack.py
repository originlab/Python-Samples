import originpro as op
import numpy as np
from skimage.util import invert
#load image stack
fn = op.path('e') + r'Samples\Image Processing and Analysis\*.tif'
iw=op.new_image()
iw.from_file(fn)
print(iw.frames)
#get the 3rd image
im2 = iw.to_np2d(2)
im2 *= 2
im2 = np.invert(im2)
#put it back into 2nd image
iw.from_np2d(im2, 1)
#show thumbnails
iw.set_int('NAV',1)
iw.set_str('Palette', 'Fire')
