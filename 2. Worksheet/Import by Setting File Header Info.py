'''
This example shows how to control file header. Typically the CSV connector can automatically
detect main header and column header info, but sometimes the automatic detection does not work
for certain file so you need to specify it yourself.
'''
import originpro as op

wks = op.new_sheet()
dc = op.Connector(wks)
dc.source = op.path('e')+r'Samples\Import and Export\F1.dat'
ss = dc.settings()
ss['mainheader']=5
ss['heading']=1
ss['unit']=2
#must not pass in filepath if you are controlling file header
#if file is passed in, the auto detection code will kick in to wipe out the settings above
dc.imp()

