'''
This sample shows how to set values to worksheet tree nodes, and 
then read out into a tree object. This is useful to save the metadata
of a data file. See the blog:
https://blog.originlab.com/accessing-metadata-using-python
'''

import originpro as op

# Create a new worksheet and set worksheet tree values.
wks = op.new_sheet()
wks.set_str("tree.data.name", "Larry")
wks.set_int("tree.data.age", 37)
wks.set_float("tree.data.mean", 23.56)

# Save the worksheet tree values to a tree object and print out the values.
trWks = wks.usertree
trData = trWks.find('data')
for child in trData:
    print(f'{child.tag} = {child.text}')
