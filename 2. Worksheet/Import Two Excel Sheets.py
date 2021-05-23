'''
This example shows how to import a second sheet from an Exel file with multiple sheets.
'''
import originpro as op

f = op.path('e')+r'Samples\Import and Export\United States Energy (1980-2013).xls'
wks = op.new_sheet()

#Create data connector object
dc = op.Connector(wks, dctype='Excel', keep_DC=False)

ss = dc.settings()
#1st two rows are header, followed by column name and units
ss['mainheader']=2;
labels = ss['labels']
#labels branch use an attrtibute to turn on, so from a dict, 
#special node is needed to set internal tree attribute
labels[op.attrib_key('Use')] = '1'
labels['longname'] = 1
labels['unit'] = 2

#Import the first sheet, which is "oil"
dc.imp(f, sel='Oil')

#Import a new Excel sheet as a new Origin sheet
dc.new_sheet('Natural Gas')

