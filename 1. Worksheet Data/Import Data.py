'''
This sample shows how to use from_file function to import data to worksheet
'''
import originpro as op

# file full path to import
f = op.path('e')+r'Samples\Curve Fitting\Enzyme.dat'

#assume active worksheet
wks = op.find_sheet()

# import the file into the worksheet and keep the Data Connector
wks.from_file(f)

print(wks.shape)