'''
This sample shows how to use data range to make plot.
'''
import os
import originpro as op

# Import the data file
wks = op.new_sheet()
wks.from_file(os.path.join(op.path('e'), 'Samples', 'Statistics', 'ANOVA', 'One-Way_ANOVA_indexed.dat'))

# Create a graph page
graph = op.new_graph(template='scatter')
gl=graph[0]

# Use the data range string as add_plot() argument.
plot = gl.add_plot(f'{wks.lt_range()}!(1,3)[1:20]')
plot = gl.add_plot(f'{wks.lt_range()}!(1,3)[21:40]')
plot = gl.add_plot(f'{wks.lt_range()}!(1,3)[41:60]')

gl.group()
gl.rescale()

# Customize legend
lgnd = gl.label('Legend')
lgnd.text='\l(1) class 1  \l(2) class 2  \l(3) class 3'
lgnd.set_int('left',1400)
lgnd.set_int('showframe',0)
