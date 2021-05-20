'''
This sample shows how to prepare a worksheet tree, and 
how to read the values back. This is useful to save the metadata
of a data file. See the blog:
https://blog.originlab.com/accessing-metadata-using-python
'''

import originpro as op

# Create a new worksheet and set worksheet tree values.
wks = op.new_sheet()
wks.set_str("tree.data.name", "Larry")
wks.set_int("tree.data.age", 37)
wks.set_float("tree.data.mean", 23.56)

# access the tree as a dictionary
dd = wks.userprops['data']
user=dd['name']
value=dd['age']
print(f'{user} is {value}')

# you can also get the tree as an xml ElementTree for more advanced usage
trWks = wks.usertree
trData = trWks.find('data')
for child in trData:
    print(f'{child.tag} = {child.text}')
    
# how to put a modified tree to another sheet
wk2 = op.new_sheet()
age_node=trData.find('age')
age_node.text='47'

wk2.usertree=trWks
print(wk2.userprops['data']['age'])
