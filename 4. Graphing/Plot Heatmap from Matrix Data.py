'''
This sample shows how to plot a heatmap from matrix data 
It shows how to set matrix xy map and how to set plot colormap
'''

import originpro as op
import numpy as np

arr_x = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
wks = op.new_sheet(type='m')
wks.from_np(arr_x)
x1,x2,y1,y2 = 0.5, 2.5, 0.5, 4.5
wks.xymap = x1,x2,y1,y2
print(wks.xymap)
gr = op.new_graph(template='Heat_Map.otpu')
gl_1 = gr[0]
plot = gl_1.add_mplot(wks, 0, type = 105)
#heatmap is showing data point at the center, so need to adjust for half step size
hs = 0.5 * (x2-x1)/2;
gl_1.set_ylim(y1-hs, y2+hs, 1)
gl_1.set_xlim(x1-hs, x2+hs, 1)
#set plot colormap
z = plot.zlevels
z['minors'] = 2
z['levels'] = [1, 3,7, 8]
plot.zlevels = z
plot.colormap = 'BlueYellow.pal'
