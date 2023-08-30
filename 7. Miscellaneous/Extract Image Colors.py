'''
This sample picks all colors from an image. 
The RGB values for each color is output to a worksheet. 
This example requires Python package extcolors to be preinstalled.
'''
import extcolors
import numpy as np
import originpro as op

# choose an image to extract colors
file_path = op.file_dialog('*.png;*.jpg;*.bmp','Select an Image')
if len(file_path) ==0:
    raise ValueError('user cancel')
    
colors = extcolors.extract_from_path(file_path)

# rgb = colors[:,0]
rgb = map(list, zip(*colors))

# print(rgb)
r = []
g = []
b = []
for row in rgb:
    r.append(row[0])
    g.append(row[1])
    b.append(row[2])

# output colors
wks = op.new_sheet()
wks.from_list(0, r)
wks.from_list(1, g)
wks.from_list(2, b)