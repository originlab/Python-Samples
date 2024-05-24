'''
This sample shows how to format graphs
'''
import originpro as op

# make a scatter plot
wks = op.new_sheet()
wks.from_file(op.path('e') + 'Samples\Graphing\Group.dat')
graph = op.new_graph(template='Scatter')
gl = graph[0]
plot = gl.add_plot(wks, coly=1, colx=0)
gl.rescale()

# change layer background color
# use set_* to access object's LabTalk property
gl.set_int('color', 7)

# change plot color
plot.color = 2

# show grid lines
gl.set_int('x.showgrids',1)
gl.set_int('y.showgrids',1)

# show axis opposite line
gl.set_int('x.opposite',1)
gl.set_int('y.opposite',1)