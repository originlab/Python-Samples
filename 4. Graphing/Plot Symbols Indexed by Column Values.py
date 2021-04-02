'''
This sample creates a scatter plot from the A(x) B(y) and control plot symbols from:
col(C) = color index (1=black,2=red etc), offset = 1 from Y which is col(B)
col(D) or col(4), or offset=2 from col(B) = symbol type and so on
modi_col is for genreal modifier control
color_col is specific to color which can further control color types, index, direct RGB, colormap
'''
import originpro as op
wks = op.new_sheet();
wks.cols=6
x=[1,2,3,4,5]
for i in range(6):
    wks.from_list(i,x)

graph = op.new_graph(template='scatter')
layer = graph[0]
plot = layer.add_plot(wks, coly=1, colx=0)
layer.rescale()
plot.color = op.color_col(1, 'n')# the +1 column, n=index
plot.symbol_kind = op.modi_col(2)
plot.symbol_size = op.modi_col(3)
plot.symbol_sizefactor=10
plot.symbol_interior = op.modi_col(4)

