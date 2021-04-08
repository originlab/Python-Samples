'''
This sample shows the management of folders under Project Explorer. It sets up same
folder structure as the /Sample/Python/ and create a workbook under each sub folder. 
'''
import os
import originpro as op

# Get the path string of a folder
path = os.path.join(op.path('e'), 'Samples', 'Python')

# Start a new project and go to the root folder in Project Explorer
op.new() 
op.pe.cd('/UNTITLED')

# Loop over subfolders under /Samples/Python/ and create subfolders with same name.
for f in os.listdir(path):
    fd = f'{os.path.splitext(f)[0]}'
    op.pe.mkdir(fd)
    op.pe.cd(f'"{fd}"')
    op.new_sheet('w',fd)
    op.pe.cd('/UNTITLED')
    
    
