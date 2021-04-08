'''
This sample shows how to make multi-layer graph with Python 
where data on each layer is from different worksheet.
'''
import os
import originpro as op

# Input three data files into three worksheets within one workbook
wb = op.new_book()
wb.set_int('nLayers',3) # Set number of sheets
for wks, fn in zip(wb, ['S15-125-03.dat', 'S21-235-07.dat', 'S32-014-04.dat']):
    wks.from_file(os.path.join(op.path('e'), 'Samples', 'Import and Export', fn))

# Add data plots onto the graph
gp = op.new_graph(template='PAN2VERT')  # load Vertical 2 Panel graph template

# Loop over layers and worksheets to add individual curve.
for i, gl in enumerate(gp):
    for wks in wb:
        plot = gl.add_plot(wks,1+i)
    gl.group()
    gl.rescale()
    

