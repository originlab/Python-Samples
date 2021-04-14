import originpro as op
wks = op.new_sheet()
fn=op.path('e') + 'Samples\Curve Fitting\Enzyme.dat'
wks.from_file(fn, False)
#add two more columns since function requires x to be 1/[S] and y to be 1/V.
#and make the two new columns as XY and set the formula S=col(A), V=col(C)
wks.cols=5
wks.cols_axis('xy',3)
wks.set_formula(3, '1/A')
wks.set_formula(4, '1/C')
wks.set_labels(['x2', 'v2'], col=3)

#Specify the input data range, which follows 
#the independent/dependent order in FDF (x1, x2, v1, v2)
range=f'{wks.lt_range()}!(1,4,2,5)'

model = op.NLFit('HillBurk')
model.set_range(range)
model.fit()
model.report(True)

