'''This example transfers a 3D Numpy array (four 3X3 matrices) into Origin,
the data is saved into a matrix sheet containing four matrix objects. Then
the data is extracted from the matrix sheet and saved into Numpy arrays. '''
import numpy as np
import originpro as op

arr=np.random.rand(4,3,3)

mxs=op.new_sheet('m')
mxs.from_np(arr)
mxs.show_thumbnails()

# Extract the data from the four matrix objects and save into a Numpy 3D array.
arr_3d=mxs.to_np3d()
print(arr_3d.shape)

# Extract the data from the first matrix object and save into a Numpy 2D array.
arr_2d=mxs.to_np2d(0)
print(arr_2d.shape)