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
HIL = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo4/PI/HILPIResistDegrau.csv")
PSIM = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo4/PI/PSIMPIResistDegrau.csv")
mag_plot.plot(HIL["Time"]+0.05, HIL["IL2"], '-', c='red', lineWidth=3, label='HIL')
mag_plot.plot(PSIM["Time"]-0.354, (PSIM["Ir"]-0.03)*1.04, '-', c='black', lineWidth=1, label='PSIM')
legend = mag_plot.legend(loc='best', shadow=True, fontsize='9')
mag_plot.set(title='Current amplitude degree test - Resistive load - PI + FF')
mag_plot.set(xlim=[0, 0.1], ylim=[-1.7, 1.7])
mag_plot.grid(True, which='minor', axis='both')
plt.savefig('HILxPSIM_comp.png', dpi=1000)


fig2 = plt.figure()
mag_plot = fig2.add_subplot(111)
plt.grid(True)
mag_plot.plot(HIL["Time"]+0.05, HIL["IL2"], '-', c='red', lineWidth=3)
mag_plot.plot(PSIM["Time"]-0.354, (PSIM["Ir"]-0.03)*1.04, '-', c='black', lineWidth=1)
mag_plot.set(xlim=[0.04825, 0.0524], ylim=[1.05, 1.5])
plt.savefig('HILxPSIM_comp_zoom.png', dpi=1000)

