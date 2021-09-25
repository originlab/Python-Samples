
import originpro as op
from sklearn.datasets import load_digits
digits = load_digits()  # load digit images, total 1797 images, each is 8x8
aa = digits.images.astype(dtype='uint8')
iw = op.new_image() 
iw.setup(1, True)  # set image window is gray scale, with multiple frames
data = aa[0:10,:,:]
iw.from_np(data, False)
iw.set_int('GrayMax',15) #set to show only 16 colors (0-15)
iw.set_int('nav', 3)  # Show navigation bar as slider
iw.set_str('Palette', 'Fire')
