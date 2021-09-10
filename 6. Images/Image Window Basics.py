import originpro as op
#single image
fn = op.path('e') + r'Samples\Image Processing and Analysis\car.bmp'
iw=op.new_image()
iw.from_file(fn)
print(f'channels {iw.channels}, size {iw.size}, type {iw.type}')
iw.rgb2gray()
print(f'after convert to grayscale, channels {iw.channels}, frames {iw.frames}')

#load multiple as image stack
fn2 = op.path('e') + r'Samples\Image Processing and Analysis\*.tif'
iw2=op.new_image()
iw2.from_file(fn2)
print(f'channels {iw2.channels}, size {iw2.size}, type {iw2.type}, frames {iw2.frames}')
#show image thumbnails(1), 2=play control, 3=slider
if iw2.type > 1:
    iw2.set_int('NAV', 1)

