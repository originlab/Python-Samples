'''
This sample plots a whole worksheet as XY plot and control plots in group
'''
import os
import originpro as op

wks = op.new_sheet()
wks.from_file(os.path.join(op.path('e'), 'Samples', 'Graphing', 'Group.dat'))
graph = op.new_graph(template='scatter')
gl=graph[0]

# plot whole sheet as XY plot
plot = gl.add_plot(f'{wks.lt_range()}!(?,1:end)')

# group the plots and control plots setting in group
gl.group()
plot.colormap = 'Candy'
plot.shapelist = [3, 2, 1]
gl.rescale()

# Customize Legend
lgnd = gl.label('Legend')
lgnd.set_int('fsize', 22)
lgnd.set_int('left',1400)
lgnd.set_int('top',700)
lgnd.set_int('showframe',0)