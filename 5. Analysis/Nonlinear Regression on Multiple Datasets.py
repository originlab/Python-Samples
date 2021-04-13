'''
This sample is to show how to run non-linear regression on multiple datasets and output 
the fitted result.
'''

import originpro as op
import pandas as pd

# Import data file
wb = op.new_book()
wks = wb[0]
fn=op.path('e') + 'Samples\Curve Fitting\Step01.dat'
wks.from_file(fn, dctype='Import Filter')

# Perform nonlinear curve fit on each dataset
model = op.NLFit('Asymptotic1')
nn = int(wks.cols/2)
result = []
for i in range(nn):
    col_name = wks.get_label(2*i, 'L')
    model.set_data(wks, 2*i, 2*i+1)
    model.fit()
    ret = model.result()
    result.append([col_name, ret['a'], ret['b'], ret['c'], ret['adjr']])    
df = pd.DataFrame(result, columns=['data','fit a','fit b', 'fit c', 'Adj. R-Square'])

# Generate the result
wks = op.new_sheet(lname='Result')
wks.from_df(df)
