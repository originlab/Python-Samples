'''
This sample creates a scatter plot from the A(x) B(y) and use Col(C)
as the color index, 1=black,2=red
'''
import originpro as op
wks = op.new_sheet();
ff=op.path('e')+r'Samples\Graphing\Group.dat'
wks.from_file(ff, False)
graph = op.new_graph(template='scatter')
layer = graph[0]
plot = layer.add_plot(wks, coly=1, colx=0)
layer.rescale()
plot.color = op.color_col(1, 'n')# the +1 column, n=index


