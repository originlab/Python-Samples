'''
This sample creates a scatter plot from the A(x) B(y) and use Col(C)
as the symbol kind and col(D) as size
'''
import originpro as op
wks = op.new_sheet();
wks.cols=4
x=[x for x in range(1,5)]
wks.from_list(0,x)
wks.from_list(1,x)
wks.from_list(2,x)
x=[10*x for x in range(1,5)];
wks.from_list(3,x)
graph = op.new_graph(template='scatter')
layer = graph[0]
plot = layer.add_plot(wks, coly=1, colx=0)
layer.rescale()
plot.symbol_kind = op.modifier_col()
plot.symbol_size = op.modifier_col(2)
