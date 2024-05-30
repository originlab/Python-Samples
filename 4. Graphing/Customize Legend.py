'''
This sample shows how to customize the legend
'''
import originpro as op

wks = op.new_sheet()
wks.from_file(op.path('e')+r"Samples\Graphing\Group.dat")

# plot whole sheet as XY plot
graph = op.new_graph(template='scatter')
gl = graph[0]
plot = gl.add_plot(f'{wks.lt_range()}!(?,1:end)')

# group the plots and control plots setting in group
gl.group()
plot.colormap = 'Candy'
plot.shapelist = [3, 2, 1]
gl.rescale()

# Customize Legend, use set_* function to set legend's LabTalk property
lgnd = gl.label('Legend')
lgnd.set_int('showframe', 0)

# use x/y axis end value to set legend center x/y position
xto = gl.get_float('x.to') 
yto = gl.get_float('y.to') 
lgnd.set_float('x', xto - lgnd.get_float('dx') / 2)  
lgnd.set_float('y', yto - lgnd.get_float('dy') / 2) 
