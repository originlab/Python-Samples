'''
This sample shows how to make a multi-layer graph and show legend only on the top layer and to show 
only legend for the first plot, while each layer has 3 plots.
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
    
# Customize legend
lgnd = gp[1].label('Legend')

lgnd.set_int('left',4900)
lgnd.set_int('top',100)
#must have something different from internal "\l(1) %(1)" to prevent auto expending
#so I just added a space, but you can add a caption or whatever as long as it is 
#different from the generic internal form
lgnd.text=' \l(1) %(1)'

#we only need one legend, so the one in layer1 will not be needed
gp[0].label('Legend').remove()
