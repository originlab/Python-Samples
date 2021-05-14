'''
This sample shows how to use from_file function to import text data to worksheet
'''
import originpro as op

f = op.path('e')+r'Samples\Curve Fitting\Enzyme.dat'

#assume active worksheet
wks = op.find_sheet()

#By default, CSV connector is used
wks.from_file(f)

print(wks.shape)