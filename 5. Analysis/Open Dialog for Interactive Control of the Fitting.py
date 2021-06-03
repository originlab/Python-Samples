"""
Fitting a curve on a graph and open dialog to adjust the parameters before final fitting
"""
import originpro as op

wks = op.new_sheet()
fn=op.path('e') + 'Samples\Curve Fitting\Gaussian.dat'
wks.from_file(fn, False)
graph = op.new_graph(template='scatter')
gl=graph[0]
dp = gl.add_plot(wks, 1, 0)
gl.rescale()

model = op.NLFit('Gauss')
model.set_range(dp.lt_range())
"""
dialog is modal, so wont close until OK, but you can use Minimize button 
to rollup the dialog and interact with the graph, then click Minimize again 
to open the dialog to continue
"""
model.param_box()
#after the dialog, still need to call Fit for final processing
model.fit()
rr=model.result()
#accessing parameters and errors
xc=rr['xc']
xc_err=rr['e_xc']
#accessing other fitting stats
chisqr=rr['chisqr']
adjr=rr['adjr']
print(f'AdjR2={adjr}, xc={xc}+-{xc_err}')
