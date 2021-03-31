'''
This sample creates a sample signal and uses this package to create a periodogram power spectral density plot.
This example requires certain Python packages. To check for and install if needed, 
open the Script Window (Shift+Alt+3), type the following and press Enter:
    pip -chk scipy numpy
'''
import numpy as np
from scipy import signal
import originpro as op

# periodogram power spectral density
fs = 10e3
N = 1e5
amp = 2*np.sqrt(2)
freq = 1234.0
noise_power = 0.001 * fs / 2
time = np.arange(N) / fs
x = amp*np.sin(2*np.pi*freq*time)
x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
f, Pxx_den = signal.periodogram(x, fs)

# put the data into worksheet
wks = op.new_sheet(type='w', lname='Periodogram Power Spectral')
wks.from_list(0, f, lname='Freq', units='Hz')
wks.from_list(1, Pxx_den, lname='PSD', units='V\+(2)/Hz')

graph = op.new_graph(template='line')

#log scale
graph[0].yscale = 2   

graph[0].set_xlim(begin=0, end=5000, step=1000)

#step=2 in log
graph[0].set_ylim(1e-7, 1e2, 2) 

graph[0].label('legend').remove()

#page.aa in LT, anti-alias -> On
graph.set_int('aa', 1)

# plot the data into the graph
plot = graph[0].add_plot(wks, coly=1, colx=0, type='line')
plot.color = '#167BB2'