"""
Simple example of doing a non-linear fitting without creating report sheet
"""
import originpro as op

wks = op.new_sheet()
fn=op.path('e') + 'Samples\Curve Fitting\Gaussian.dat'
wks.from_file(fn, False)


#do the fitting and receive fitting parameters. No report will be generated
model = op.NLFit('Gauss')
model.set_data(wks, 0, 1)
model.fix_param('y0', 0)
model.fit()
rr=model.result()

#accessing parameters and errors
xc=rr['xc']
xc_err=rr['e_xc']
#accessing other fitting stats
chisqr=rr['chisqr']
adjr=rr['adjr']

print(f'xc={xc}+-{xc_err}')

