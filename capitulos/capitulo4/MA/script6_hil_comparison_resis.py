import matplotlib.pyplot as plt
import pandas
import numpy as np

plt.rcParams["font.family"] = 'Times New Roman'
plt.rcParams["font.style"] = 'normal'
plt.rcParams["font.variant"] = 'normal'
plt.rcParams["font.weight"] = 'normal'
plt.rcParams["font.stretch"] = 'normal'
plt.rcParams["font.size"] = '11'

fig = plt.figure()
mag_plot = fig.add_subplot(111)
plt.grid(True)
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
HIL = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo4/MA/validacao_degrau_amplitude.csv")
PSIM = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo4/MA/validacao_degrau_amplitude_PSIM.csv")
mag_plot.plot((HIL["Time"]+0.5)/10, HIL["L2_2"], '-', c='red', lineWidth=3, label='HIL')
mag_plot.plot(PSIM["Time"]-0.0537, PSIM["Ir"], '-', c='black', lineWidth=1, label='PSIM')
legend = mag_plot.legend(loc='best', shadow=True, fontsize='9')
mag_plot.set(title='Current amplitude degree test - Resistive load - Without control')
mag_plot.set(xlim=[0, 0.1], ylim=[-2, 2])
mag_plot.grid(True, which='minor', axis='both')
plt.savefig('HILxPSIM_comp.png', dpi=1000)


fig2 = plt.figure()
mag_plot = fig2.add_subplot(111)
plt.grid(True)
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
mag_plot.plot((HIL["Time"]+0.5)/10, HIL["L2_2"], '-', c='red', lineWidth=3, label='HIL')
mag_plot.plot(PSIM["Time"]-0.0537, PSIM["Ir"], '-', c='black', lineWidth=1, label='PSIM')
legend = mag_plot.legend(loc='best', shadow=True, fontsize='9')
mag_plot.set(title='Current amplitude degree test - Resistive load - Without control (zoom)')
mag_plot.set(xlim=[0.04775, 0.05375], ylim=[0.55, 2])
mag_plot.grid(True, which='minor', axis='both')
plt.savefig('HILxPSIM_comp_zoom.png', dpi=1000)

