'''
This example shows how to use a filter created from Import Wizard
'''
import originpro as op

fn = op.path('e')+r'Samples\Import and Export\S15-125-03.dat'
wks=op.new_sheet()
#use a filter in the same folder as the data file
wks.from_file(fn, False, 'Import Filter','.\VarsFromFileNameAndHeader.oif')
