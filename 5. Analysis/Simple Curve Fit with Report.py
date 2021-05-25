"""
Simple example of doing a non-linear fitting with a report sheet
"""
import originpro as op

wks = op.new_sheet()
fn=op.path('e') + 'Samples\Curve Fitting\Gaussian.dat'
wks.from_file(fn, False)

#do the fitting and generate report
model = op.NLFit('Gauss')
model.set_data(wks, 0, 1)
model.fit()
r, c = model.report()
wReport=op.find_sheet('w', r)
wReport.activate()

