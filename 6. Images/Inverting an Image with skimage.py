#need to install "scikit-image" first
import originpro as op
import numpy as np
from skimage.util import invert

fn = op.path('e') + r'Samples\Image Processing and Analysis\Flower.jpg'
iw=op.new_image()
iw.from_file(fn)
iw.lname='original image'
#make a copy to put result
iw2=iw.duplicate()
iw2.lname='inverted'
img = iw2.to_np()
inv = invert(img)
iw2.from_np(inv)
#put into new empty image window
iw3=op.new_image()
#need to first setup the image window as 3 channels and not multi-frames
iw3.setup(3,False)
iw3.lname='invert back'
inv = invert(inv)
iw3.from_np(inv)

