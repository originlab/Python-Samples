'''
This sample shows basic data transfer between Origin matrix and a NumPy array.
Make sure you've installed pandas before trying the following sample. 
So to check for and install if needed, open the Script Window (Shift+Alt+3), 
type the following and press Enter:
    pip -chk pandas
'''
import numpy as np
import originpro as op

#integer matrix data
aa = np.array([	[1, 2, 3], [4, 5, 6] ])
bb = np.array([	[10,11], [20,21], [30,31] ])

#create a new hidden matrix book, and get the matrix sheet
ma=op.new_sheet('m')

#matrix sheet can hold a 3D array, shape and data type is automatically set 
ma.from_np(aa)

#another sheet in same book
mb = ma.get_book().add_sheet()
mb.from_np(bb)

#put result into 3rd sheet
mc = ma.get_book().add_sheet('Dot Product')

#do the actual calculation using numpy
#here each sheet has only one matrix object, so we get it as 2d array
cc = np.dot(ma.to_np2d(), mb.to_np2d())
mc.from_np(cc)

