'''
Import each data file in a sample folder into an Analysis Template and
perform the fitting and update the reports with graphs, so you end up
with a book for each file in the Origin workspace for further examination
'''
import originpro as op
import pandas as pd
import os
import re


# location of sample data files that ship with Origin.
data_folder = op.path('e') + r'Samples\Curve Fitting'

# Iterate data file folder for file names to import.
for file in os.listdir(data_folder):
    if re.search('^Sensor[0-9]{2}.dat$', file):
        print(f'working on {file}')
        imp_file = os.path.join(data_folder, file)
        # Load analysis template book that ships with Origin.
        at = op.load_book(op.path('e') + r'Samples\Batch Processing\Sensor Analysis.ogw')
        # This template put Data sheet as 1st worksheet in book.
        wks = at[0]
        # Import the file into the worksheet and removing the Data Connector.
        wks.from_file(imp_file, False)

        # Wait for analysis operation to complete.
        op.wait()

        

