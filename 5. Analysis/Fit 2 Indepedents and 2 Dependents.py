import originpro as op
wks = op.new_sheet()
fn=op.path('e') + 'Samples\Curve Fitting\Enzyme2.dat'
wks.from_file(fn, False)
wks.cols_axis('x',2,2)

#Specify the input data range, which follows 
#the independent/dependent order in FDF (x1, x2, v1, v2)
range=f'{wks.lt_range()}!(1,3,2,4)'
model = op.NLFit('HillBurk')
model.set_range(range)
model.fit()
model.report(True)

