'''
This example shows importing from the web and to specify from Jan of each year
as well as doing proper longitude and latitude corrections.
'''
import originpro as op
mat = op.new_sheet('m')
#you can actually use URL in from_file 
url = 'https://www.unidata.ucar.edu/software/netcdf/examples/tos_O1_2001-2002.nc'
#keep the connector so after the import, you can click on the icon to 
#choose Options... to see open the dialog to see the details indicated by the sel string
mat.from_file(url, True, dctype='NetCDF', sel='NetCDF/tos[1:0|1-11][y#][x/2]')
