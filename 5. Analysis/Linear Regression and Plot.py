'''
This sample is to show how to run linear regression with Python in Origin. The fitted curve 
and prediction band are then plotted out.
'''

import originpro as op

# Import data file
wb = op.new_book()
wks = wb[0]
fn=op.path('e') + 'Samples\Curve Fitting\Linear Fit.dat'
wks.from_file(fn,False)

#Perform linear fit 
lr = op.LinearFit()
lr.set_data(wks, 0, 1)
lr.fix_intercept(0.1)
r, c = lr.report(3) # Return the result report sheet and fitted curve sheet.
wReport=op.find_sheet('w', r)
wCurves=op.find_sheet('w', c)

# Plot the fitted curve and prediction band
gp = op.new_graph()
gl = gp[0]

gl.add_plot(wCurves, 1, 0) # Plot the fitted line

# Add the prediction band
plt1 = gl.add_plot(wCurves, 4, 0) 
plt1.transparency = 80
plt2 = gl.add_plot(wCurves, 5, 0)
plt2.transparency = 80
plt1.set_fill_area(2,9,2) # fill the color to the next plot

gl.rescale()

