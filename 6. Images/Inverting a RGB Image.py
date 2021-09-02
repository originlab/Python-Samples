import originpro as op
import numpy as np
from skimage.util import invert

folder = op.path('e') + r'Samples\Image Processing and Analysis'
fn = folder + r'\Flower.jpg'

op.lt_exec('win -n image')
im=op.find_image()
im.from_file(fn)
op.lt_exec('win -d')
im=op.find_image()

original = im.to_np()
inv = invert(original)
im.from_np(inv)
