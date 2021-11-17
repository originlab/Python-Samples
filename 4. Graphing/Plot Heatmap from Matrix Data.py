'''
This sample shows how to plot a heatmap from matrix data 
It also shows how to set matrix xy map and how to set plot colormap
'''
import originpro as op
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
mat = op.new_sheet(type='m')
mat.from_np(arr)
x1,x2,y1,y2 = 0.5, 2.5, 0.5, 4.5
mat.xymap = x1,x2,y1,y2
gr = op.new_graph(template='Heat_Map.otpu')
g = gr[0]
p = g.add_mplot(mat, 0, type = 105)
#heatmap is showing data point at the center, so need to adjust for half step size
hs = 0.5 * (x2-x1)/2;
g.set_ylim(y1-hs, y2+hs, 1)
g.set_xlim(x1-hs, x2+hs, 1)
#set plot colormap
z = p.zlevels
z['minors'] = 2
z['levels'] = [1, 3,7, 8]
p.zlevels = z
p.colormap = 'BlueYellow.pal'
