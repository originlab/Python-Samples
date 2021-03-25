'''
This example shows how to import tif images into a 3d numpy array and then pass into Origin matrix book.
To install openCV (cv2), do the following from Script Window
    pip install opencv-python
'''
import originpro as op
import numpy as np
import cv2

# import tifs into array
# Assume all images share the same dimesion
ImArray = np.array([])
for idx in range(7):
    fname = op.path('e') + f'Samples\\Image Processing and Analysis\\myocyte{idx+1}.tif'
    array = np.array(cv2.imread(fname, cv2.IMREAD_UNCHANGED))
    ImArray = np.dstack((ImArray, array)) if ImArray.size else array

# put this 3d array into Origin Matrix Sheet
ms = op.new_sheet('m')
ms.from_np(arr=ImArray, dstack=True)
ms.show_slider(True)
ms.show_image(True)

