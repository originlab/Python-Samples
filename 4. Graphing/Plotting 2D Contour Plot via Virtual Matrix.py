'''
This sample shows how to use virtual matrix to make a contour plot
'''
import originpro as op

# new a graph with Contour template
gp = op.new_graph(template='Contour')

# prepare data
wks = op.new_sheet()
wks.from_file(op.path('e')+"Samples\Graphing\VSurface 1.dat")

# use LabTalk call plotvm X-Function
# 226 = IDM_PLOT_CONTOUR
# add plot to gp's first layer
ltStr = r'plotvm irng:=1! format:=xacross rowpos:=selrow1 colpos:=selcol1 ztitle:="VSurface 1" type:=226 ogl:='+ f'{gp[0]}!'
op.lt_exec(ltStr)

# set X scale type to Log10 
gp.activate()
gp[0].xscale=2
gp[0].set_xlim(11, 100)
gp[0].set_ylim(3, 7)