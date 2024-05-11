'''
This sample shows how to merge Graph1, Graph2...... Graph10
'''
import originpro as op

ids = list(range(1,11))
graphs = ["Graph" + str(i) for i in ids]
graphs = '\n'.join(graphs)

ltStr = f'merge_graph option:=specified option:=specified graphs:="{graphs}" row:=2 col:=5;'
op.lt_exec(ltStr)