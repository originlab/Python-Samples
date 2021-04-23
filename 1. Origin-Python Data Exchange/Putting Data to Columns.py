'''
This sample shows how to use from_list function to put data to Columns
'''
import originpro as op

# Prepare data.
data=[x/10. for x in range(50)]

# Prepare worksheet.
wks=op.new_sheet()

# Put data to col(A), and set Long Name, Units, designation as well
wks.from_list('A',data, 'time', 'sec',axis='N')

# Prepare data and out data to col(B)
data1=[x*1.5 for x in range(50)]
wks.from_list('B', data1, axis='X')

# Add a third column
wks.cols=3

# Use the sum of data and data1 to set the third column
wks.from_list(2, [sum(i) for i in zip(data, data1)], comments = 'A+B')

