'''
This example shows how to do partial import with CSV data connector
'''
import originpro as op

f = op.path('e')+r'Samples\Import and Export\S15-125-03.dat'
wks = op.new_sheet()

#Specify the rows to import
dc = op.Connector(wks, keep=True) #Add data connector
ss = dc.settings()
partial = ss['partial']
partial[op.format_attrib_key('Use')]='1'
partial['row']='10:20'

#Import
dc.imp(f)


