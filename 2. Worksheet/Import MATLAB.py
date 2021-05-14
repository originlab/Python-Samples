'''
This sample shows how to import MATLAB file.
You can try different selection by using GUI
'''

import originpro as op
fn = op.path('e')+r'Samples\Import and Export\GaussianData.mat'
wks=op.new_sheet()

wks.from_file(fn, True, 'MATLAB', 'MATLAB/Data')
