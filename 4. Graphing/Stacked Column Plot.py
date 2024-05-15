'''
This sample shows how to make a stacked cloumn plots
'''
import originpro as op

# import data
wks = op.new_sheet()
wks.from_file(op.path('e') + 'Samples\Graphing\Group.dat')

# add plots and group the plots
graph = op.new_graph(template='StackColumn')
gl = graph[0]
gl.add_plot(wks, coly=1, colx=0, type='?')
gl.add_plot(wks, coly=2, colx=0, type='?')
gl.group(True, 0, 1)

# set stack offset of plots to Cumulative
gl.lt_exec('layer -b s 1')

# set column plot gap
gl.lt_exec('set %C -vg 40')