'''
This sample shows how to prepare worksheet for plotting. 
'''
import originpro as op

#Import Data File
f = op.path('e')+r'Samples\Signal Processing\Sunspot.dat'
wks = op.new_sheet()
wks.from_file(f, keep_DC=False)

#Set worksheet property
wks.cols=5
wks.move_cols(1,2,1) #Insert a date column
wks.cols_axis('xyy',2,4) #Set column designation

#Set "Date" column property
ncol=2
wks.set_formula(ncol,'date(B$ + "/1/" + A$)')
wks.set_label(ncol, 'Date')
wks.as_date(ncol,"yyyy/MM")

#Set "Averaged Sunspot Number" column property
ncol=4
wks.set_formula(ncol,'movavg(D,20,20)')
wks.set_label(ncol, 'Averaged Sunspot Number')

#Plot "Sunspot Number" vs "Date"
gp = op.new_graph()
gp[0].add_plot(f'{wks.lt_range()}!(3,4:5)')  # Plot using data range
gp[0].group()
gp[0].rescale()

