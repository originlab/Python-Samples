'''
This example splits a dataset with multiple columns to two datasets named Train and Test, 
using the package sklearn. To check for and install if needed, 
open the Script Window (Shift+Alt+3), type the following and press Enter.
 pip -chk pandas sklearn
'''
import numpy as np
import pandas as pd
import originpro as op
from sklearn.model_selection import train_test_split

# Import data and get the independent and dependent data to X and y respectively
ws=op.new_sheet()
ws.from_file(fname=op.path('e')+r"Samples\Statistics\Fisher's Iris Data.dat", keep_DC=False)

# Get first 4 columns as X
X = ws.to_df(c1=0, numcols=4)  

# Get the last column as y
y = ws.to_df(c1=4, numcols=1)  

# Split the dataset into train and test datasets
# train dataset contains 70% samples, and test dataset contains 30% samples
# shuffle the data before splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True, random_state=1)

# Create worksheet for the splitted datasets
wks = op.new_sheet('w', 'Split')
Num = X_train.columns.shape[0]
wks.from_list(Num, y_train.iloc[:, 0].tolist(), comments='Train', lname=y_train.columns[0])
wks.from_list(Num*2+1, y_test.iloc[:, 0].tolist(), comments='Test', lname=y_train.columns[0])
for idx in range(Num):
    wks.from_list(idx, X_train.iloc[:, idx].tolist(), comments='Train', lname=X_train.columns[idx])
    wks.from_list(Num+1+idx, X_test.iloc[:, idx].tolist(), comments='Test', lname=X_train.columns[idx])