'''This sample shows how to plot a heatmap from a matrix sheet.'''
import originpro as op
import numpy as np

arr_2D = np.random.randint(0,4, size=(4,4))
ms = op.new_sheet('m')
ms.from_np(arr_2D)
ms.xymap = -3, 3, -3, 3
gp = op.new_graph(template='heatmap')
gp[0].add_plot(ms, colz=0)
gp[0].rescale('z')
#default XY scale will include the half width of each data point
#so to have same scale as the matrix, we need to force it
gp[0].set_xlim(-3, 3)
gp[0].set_ylim(-3, 3)
