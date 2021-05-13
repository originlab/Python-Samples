'''
This sample loops through all the worksheets in the project,
print out the number of rows of each sheet.
'''
import originpro as op

for wb in op.pages('w'):
    for wks in wb:
        print(f'Worksheet {wks.lt_range()} has {wks.rows} rows')
        
