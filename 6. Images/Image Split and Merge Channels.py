import originpro as op

fn = op.path('e') + r'Samples\Image Processing and Analysis\Leaves.jpg'
iw=op.new_image()
iw.from_file(fn)
iw.split()
g = iw.to_np2d(1)
g *= 0
iw.from_np2d(g, 1)
iw.merge()
iw.lname='Green is removed'

