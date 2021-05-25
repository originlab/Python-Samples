"""
Simple example of doing a non-linear fitting with a report sheet
"""
import originpro as op

wks = op.new_sheet()
fn=op.path('e') + 'Samples\Curve Fitting\Gaussian.dat'
wks.from_file(fn, False)
graph = op.new_graph(template='scatter')
gl=graph[0]
dp = gl.add_plot(wks, 1, 0)
gl.rescale()

#do the fitting and generate report
model = op.NLFit('Gauss')
model.set_range(dp.lt_range())
model.fit()
r, c = model.report()
wReport=op.find_sheet('w', r)
wReport.activate()
