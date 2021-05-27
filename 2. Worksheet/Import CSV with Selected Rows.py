'''
This example shows how to do partial import with CSV data connector
'''
import originpro as op

f = op.path('e')+r'Samples\Import and Export\S15-125-03.dat'
wks = op.new_sheet()

#Use CSV connector which is the default
#and connector will be removed after import
dc = op.Connector(wks)

#Specify the rows to import
ss = dc.settings()
partial = ss['partial']
partial[op.attrib_key('Use')]='1'
partial['row']='10:20'

#import from rwo 10 to row 20
dc.imp(f)


