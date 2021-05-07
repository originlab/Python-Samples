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
lr.fix_intercept(-0.7)
r, c = lr.report(3) # Return the result report sheet and fitted curve sheet.
wReport=op.find_sheet('w', r)
wCurves=op.find_sheet('w', c)

# Plot the data and fitted curve and confidence band
gp = op.new_graph()
gl = gp[0]

# Plot data as scatter plot
pltdata = gl.add_plot(wks, 1, 0, type='s')

# Add the confidence band
conf = gl.add_plot(wCurves, 2, 0) 
gl.add_plot(wCurves, 3, 0)

# Group the newly added plots, starting from 1 to skip the scatter data
gl.group(True, 1)
conf.colorinc=0
conf.transparency = 80
conf.set_fill_area(op.ocolor('Red')) # fill the color to the next plot

gl.add_plot(wCurves, 1, 0) # Plot the fitted line

gl.rescale()

# Customize legend
lgnd = gl.label('Legend')
lgnd.text='\\l(4) Linear Fit\n\\l(2) Confidence Band'
lgnd.set_int('left',1400)
lgnd.set_int('top',700)
lgnd.set_int('showframe',0)
