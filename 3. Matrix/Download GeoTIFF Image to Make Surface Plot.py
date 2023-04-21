'''
Origin2023b or later is required to run this sample code.

This example shows how to use Origin Image Window's ability to directly import an image using
a URL address, which is not yet supported in a matrix window. Once image is downloaded into an
Image Window, it can be converted to a matrix with the coordinates from the GeoTIFF retained.
The sample also shows to download a graph template from Originlab to make our plot
'''
import originpro as op
#use the smaller 2-arc sec DEM available only for Alaska from National Map
url = r'https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/2/TIFF/historical/n59w154/USGS_2_n59w154_20210401.tif'
iw=op.new_image()
iw.from_file(url)
#create an empty matrix and tranfer the image to it
mat = op.new_book('m')
mat[0].from_img(iw)
#you may want to keep the image window and comment out the next line but 
#it is no longer needed to make the graph
iw.destroy()
#On Template Center dialog, click any template will open the weblink to see the fid
#here 939 = RaisedReliefMap.otpu
nn=op.olab_download(939)
if nn < 0:
    raise Exception("Sorry, failed to download template from Originlab website")
    
gp = op.new_graph(template='RaisedReliefMap')

#we need to turn on speed mode and hide the speed mode banner
gp.set_int('Banner', 0)
gl = gp[0]
gl.set_int('MatMaxPtsEnabled', 1)
plot = gl.add_mplot(mat[0], 0)
gl.rescale()

#if template did not have clip data enabled
#gl.set_int('clip',1)

plot.colormap = 'Magma.PAL'
ax=gl.axis('x')
ax.sto=-153.2
ay=gl.axis('y')
ay.set_limits(58.4,59)

gl.set_int('light.direction.h', 74)
gl.set_int('light.direction.v', 27)

