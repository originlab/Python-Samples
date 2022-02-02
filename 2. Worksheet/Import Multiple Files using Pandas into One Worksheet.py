# Usage
# =====
# Script concatenates multiple NetCDF files into one file.
# Instructions:
#   1. Put all *.NC files you want to process into an input folder.
#   2. Run this script.
#   3. You will be prompted for an input folder.
#   4. You will then be prompted for an output file.
#       Do NOT choose the input folder.
#
# Note: If large number of files, it may take quite some time to run.
#
# Note: All files to concatenate must have the same structure and
#   and variable dimensions. Also, all files must have a dimension
#   such as `time` in order for the concatenation to work.

"""
Simple example of doing a non-linear fitting without creating report sheet
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
    wks.set_labels(df.columns.get_level_values(0), 'L', col)
    wks.set_labels(df.columns.get_level_values(1), 'U', col)
    comments = df.columns.get_level_values(2).tolist()
    comments[0] = ""
    wks.set_labels(comments, 'C', col)
    col = wks.cols
