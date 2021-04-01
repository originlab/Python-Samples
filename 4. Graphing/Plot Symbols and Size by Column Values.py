'''
This sample creates a scatter plot from the A(x) B(y) and use Col(C)
as the symbol kind and col(D) as size
'''
import originpro as op
wks = op.new_sheet();
wks.cols=5
x=[x for x in range(1,5)]
for i in range(5):
    wks.from_list(i,x)

graph = op.new_graph(template='scatter')
layer = graph[0]
plot = layer.add_plot(wks, coly=1, colx=0)
layer.rescale()
plot.symbol_kind = op.modi_col(1)
plot.symbol_size = op.modi_col(2)
plot.symbol_sizefactor=10
plot.symbol_fill = op.modi_col(3)


