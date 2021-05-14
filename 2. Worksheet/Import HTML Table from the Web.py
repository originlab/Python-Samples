'''
Despite the name, from_file can actually import from the web
This example shows using the HTML connector to import a specific table 
from a wikipedia web page
'''
import originpro as op
fn = 'https://en.wikipedia.org/wiki/World_population'
wks=op.new_sheet()
wks.from_file(fn, True, 'HTML', 'Tables/_6')

