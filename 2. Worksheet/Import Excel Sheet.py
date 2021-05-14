'''
This example shows how to Customize the Excel data connector.
1. Parse headerlines to column labels.
2. Import partial cols and rows.
3. Specify the spreadsheet to import.
'''
import originpro as op

f = op.path('e')+r'Samples\Import and Export\Partial Import.xlsx'
wks = op.new_sheet()

#Create data connector object
dc = op.Connector(wks, dc='Excel', keep=True)
ss = dc.settings()

#Headerlines to column label
labels = ss['labels']
labels[op.attrib_key('Use')] = '1'
labels['longname'] = 1
labels['unit'] = 2

#Setting for partial import
partial = ss['partial']
partial[op.attrib_key('Use')] = '1'
partial['col'] = '1:3'
partial['row'] = '1:99'

#Import the second spreadsheet 'expt2'
dc.imp(f, sel='expt2')

