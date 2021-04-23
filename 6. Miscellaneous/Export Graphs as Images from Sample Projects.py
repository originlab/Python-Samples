'''
This sample generate an image from a graph from a sample project. 
Please note that a file named my_py_test.png will be replaced by running this sample.
'''
import originpro as op

#from Learning Center folder
op.open(op.path('c')+ r'\Graphing\Trellis Plots - Box Charts.opju')

gg=op.find_graph(0)

# export graph to an image
f=''
if gg:
    f=gg.save_fig(op.path()+'my_py_test.png',width=500)

import os
if len(f):
    os.startfile(f)