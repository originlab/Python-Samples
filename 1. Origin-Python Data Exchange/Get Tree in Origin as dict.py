'''
To show how to get a Tree in Origin. 
Tree variables are used extensively inside Origin. In this example, we use an X-Function
which will generate a Tree after its execution. The Tree will have the same name as the 
X-Function, which in the sample below is "fitlr". It does a simple linear fit and generates
basic stats fromt the fit, see
https://www.originlab.com/doc/X-Function/ref/fitLR
'''
import originpro as op
fn=op.path('e') + 'Samples\Curve Fitting\Linear Fit.dat'
wks = op.new_sheet()
wks.from_file(fn,False)
#fit A(x) D(y)
wks.get_book().lt_exec('fitlr (A,D)')
dd = op.lt_tree_to_dict('fitlr')
slope = dd['b']
err = dd['berr']
print(f'slope= {slope:.3f} +- {err:.3f}')
