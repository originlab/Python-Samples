'''
This sample shows how to use report_table function to
access a table in an Analysis Report Sheet
'''
import originpro as op
import pandas as pd
import os
import re

# Load analysis template book that ships with Origin.
at = op.load_book(op.path('e') + r'Samples\Batch Processing\Sensor Analysis.ogw')

# Get 1st worksheet in book.
wks = at[0]
wks_table = at[1]
df_list = []

# Get folder for data files that ship with Origin.
data_folder = op.path('e') + r'Samples\Curve Fitting'

# Iterate data file folder for file names to import.
for file in os.listdir(data_folder):

    # Filter for specific data files.
    if re.search('^Sensor[0-9]{2}.dat$', file):

        # Full path to file to import.
        imp_file = os.path.join(data_folder, file)

        # Import the file into the worksheet and removing the Data Connector.
        wks.from_file(imp_file, False)

        # Wait for analysis operation to complete.
        op.wait()

        # If  you want to see live updates of the graph, add the line below.
        #op.wait('s', 0.1)
        
        df = wks_table.report_table('Summary')
        df.iloc[:, 0] = file
        
        df_list.append(df)

        print(f'working on {file}')
        
result = pd.concat(df_list)
wks_result = op.new_sheet()
wks_result.from_df(result)

