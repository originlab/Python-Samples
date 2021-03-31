'''
This sample shows how to set Column Format with DataFrame and from_df, to_df functions.
Make sure you've installed pandas. To install the module, 
open the Script Window (Shift+Alt+3), type the following and press Enter:
 pip install pandas

The following will check and install:
 pip -chk pandas
'''
import originpro as op
import pandas as pd

# Create a dataframe to fill the sheet
df = pd.DataFrame({
    'Date': ['10/25/2018','02/21/2019','04/01/2020'],
    'Gender':['Male','Male','Female'],
    'Score': [75.5, 86.7, 91],
})

df['Date'] = pd.to_datetime(df['Date'])
df['Gender']= pd.Categorical(df['Gender'])

wks=op.new_sheet()
wks.from_df(df)

#can also create book and get first sheet like this
wks2=op.new_book('w', 'Copy using DF')[0]

#column formats like date is automatically handled
df1=wks.to_df()
wks2.from_df(df1)