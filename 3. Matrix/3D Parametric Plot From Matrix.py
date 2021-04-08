'''This sample shows how to plot parametric 3D surface from a matrix sheet.'''
import originpro as op
import numpy as np

# Generate torus mesh
angle = np.linspace(0, 2*np.pi, 32)
theta, phi = np.meshgrid(angle, angle)
r, R = .25, 1.
X = (R + r * np.cos(phi)) * np.cos(theta)
Y = (R + r * np.cos(phi)) * np.sin(theta)
Z = r * np.sin(phi)
arr_3D = np.stack([Z,X,Y], axis=0) # Stack X,Y,Z to get a 3D array

# Pass the data to a matrix sheet and plot
ms = op.new_sheet('m')
ms.from_np(arr_3D)

gp = op.new_graph(template='GLparafunc')
gp[0].add_mplot(ms,0,1,2)
gp[0].rescale('z')

