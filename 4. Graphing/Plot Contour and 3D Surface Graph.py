'''
This sample shows how to plot contour and 3D colormap surface from XYZ data. 
The Graph template names and IDs can be found in the page:
https://www.originlab.com/doc/LabTalk/ref/Plot-Type-IDs
'''
import originpro as op

#Import Data File
wks = op.new_sheet()
f = op.path('e')+r'Samples\Matrix Conversion and Gridding\XYZ Random Gaussian.dat'
wks.from_file(f)
wks.cols_axis('xyz') 

# Plot 3D surface
gp = op.new_graph(template='glCMAP')
p = gp[0].add_plot(wks,coly=1,colx=0,colz=2, type=103) 
gp[0].rescale()

# Plot contour
gp = op.new_graph(template='TriContour')
p = gp[0].add_plot(wks,coly=1,colx=0,colz=2, type=243)
p.colormap = 'Maple.pal'
gp[0].rescale()