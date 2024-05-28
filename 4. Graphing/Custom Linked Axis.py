'''
This sample shows how to customize the linked axis to make a functionally mapped double-X graph
'''
import originpro as op

graph = op.new_graph()
gl = graph[0]
gl.axis('x').title='Fahrenheit'

# add Top-X layer 
gl2 = graph.add_layer(1)

# use LabTalk change top axis' title
op.lt_exec('xt.text$=Celsius')

# mapped Double-X, Fahrenheit to Celsius conversion
gl2.set_str('x.link.from', '(X1-32)/1.8')
gl2.set_str('x.link.to', '(X2-32)/1.8')
gl2.set_int('x.showgrids',1)
gl2.set_int('x.grid.majorType',2)

# use temperature data to plot
wks = op.new_sheet()
wks.from_file(op.path('e')+r"Samples\Statistics\temperature.dat")
gl.activate()
gl.add_plot(wks, coly=1, colx=0, type='s')
gl.rescale()