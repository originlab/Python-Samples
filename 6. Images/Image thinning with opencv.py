import cv2
import numpy as np
import originpro as op

fn = op.path('e') + r'Samples\Image Processing and Analysis\car.bmp'
iw=op.new_image()
iw.from_file(fn)
iw.lname='original image'
iw.rgb2gray()
#make a copy to put result
iw2=iw.duplicate()
iw2.lname = 'thinning result'
img = iw2.to_np()
# Structuring Element
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# Create an empty output image to hold values
thin = np.zeros(img.shape,dtype='uint8')
 
# Loop until erosion leads to an empty set or max
max = 20
while (cv2.countNonZero(img)!=0):
    # Erosion
    erode = cv2.erode(img,kernel)
    # Opening on eroded image
    opening = cv2.morphologyEx(erode,cv2.MORPH_OPEN,kernel)
    # Subtract these two
    subset = erode - opening
    # Union of all previous sets
    thin = cv2.bitwise_or(subset,thin)
    # Set the eroded image for next iteration
    img = erode.copy()
    max -= 1
    if max == 0:
        break

iw2.from_np(thin)
