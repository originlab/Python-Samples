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
