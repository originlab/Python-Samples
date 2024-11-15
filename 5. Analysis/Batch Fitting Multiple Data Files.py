'''
This sample is to show how to run gaussian peak fit on multiple data files. 
Then the fitted peak parameters xc, w, A are plotted as a function of temperature
in a three Y axes graph.
'''

import originpro as op
import numpy as np

# One worksheet for imported data, one worksheet for peak fitting result
wks = op.new_sheet()
wks_result = op.new_sheet()


wts = [0, 25, 100, 150, 250]
for i, wt in enumerate(wts):    
    # Import each data file into wks
    fd = op.path('e') + 'Samples\Batch2'
    fn = f'{fd}\Sample 2 {wt} wt.txt'
    wks.from_file(fn, keep_DC=False)
    
    # Baseline subtraction
    spec = wks.to_list(1)
    spec = np.array(spec)
    base = np.linspace(spec[0], spec[-1], len(spec)) # straight line connecting start and end point as baseline
    spec = spec - base
    wks.from_list(1, spec)      
    
    # Run Gaussian fit on subtracted spectrum
    model = op.NLFit('Gaussian')
    model.set_data(wks, 0, 1)
    model.fix_param('y0',0)
    model.fit()
    ret = model.result()
    
    # Fitting result is saved to each row of wks_result
    wks_result.from_list2([wt, ret['xc'], ret['w'], ret['A'], ret['adjr']], i) 
    
wks_result.set_labels(['temperature','fit x','fit width', 'fit area', 'Adj. R-Square'])

# Plot the data
gp = op.new_graph(template='3Ys_Y-YY')
for i in range(3):    
    gp[i].add_plot(wks_result,1+i,0)
    gp[i].rescale()

# Customize Legend
lgnd = gp[0].label('Legend')
lgnd.text='\l(1.1) %(1.1)   \l(2.1) %(2.1)   \l(3.1) %(3.1)'
lgnd.set_int('fsize', 27)
lgnd.set_int('top', 400)