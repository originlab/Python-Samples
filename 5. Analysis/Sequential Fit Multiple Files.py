'''
Import each data file in a sample folder into and perform fitting with parameters dialog
to check each fit and generate a sheet with result parameters and stats.
'''
import originpro as op
import os

data_folder = op.path('e') + r'Samples\Batch Processing'
#only to process 3 files
names = ['T285K.csv', 'T305K.csv', 'T345K.csv']
pk_centers=[]
chisqrs=[]
wdata = op.new_sheet()
graph = op.new_graph(template='scatter')
gl=graph[0]
model = op.NLFit('Gauss')
for file in names:
    f = os.path.join(data_folder, file)
    print(f'working on {f}')
    wdata.from_file(f, False)
    dp = gl.add_plot(wdata, 1, 0)
    gl.rescale()
    model.set_range(dp.lt_range())
    model.param_box()
    model.fit()
    if not op.messagebox('Take a look at the fit', True):
        break
        
    rr=model.result()
    gl.remove(dp)
    chisqrs.append(rr['chisqr'])
    pk_centers.append(rr['xc'])
    
wdata.get_book().remove()    
graph.remove()
wks = op.new_sheet()
wks.from_list(0, names, 'File Name')
wks.from_list(1, pk_centers, 'Peak Center')
wks.from_list(2, chisqrs, 'Chisqr')