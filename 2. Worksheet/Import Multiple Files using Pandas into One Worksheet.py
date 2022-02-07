"""
This shows import text files using DataFrame instead of Origin's internal import
"""
import originpro as op
import pandas as pd
import os
fd = op.path('e') + r'Samples\Batch2'
wks = op.new_sheet()
col = 0
for file in os.listdir(fd):
    df = pd.read_table(os.path.join(fd, file), header=[0,1,2])    
    wks.from_df(df, col)
    wks.cols_axis('xy', col)
    wks.set_labels(df.columns.get_level_values(0), 'L', col)
    wks.set_labels(df.columns.get_level_values(1), 'U', col)
    #the sample data file has no comment for X column, so we need to remove the 'Unnamed: 0_level_2'
    comments = df.columns.get_level_values(2).tolist()
    comments[0] = ""
    wks.set_labels(comments, 'C', col)
    col = wks.cols
