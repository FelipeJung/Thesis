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
HIL = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo4/PI_grid/HILPIConectadoRedeCap50u_.csv")
PSIM = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo4/PI_grid/PI_PSIM.csv")
mag_plot.plot(HIL["Time"]-7.708333, HIL["IL2"]*0.9, '-', c='red', lineWidth=3, label='HIL')
mag_plot.plot(HIL["Time"]-7.708333, HIL["Rede"]/311, '-', c='blue', lineWidth=2, label='Grid / 311')
mag_plot.plot(PSIM["Time"]-0.3, (PSIM["Ir"]-0.03)*1.04, '-', c='black', lineWidth=1, label='PSIM')
legend = mag_plot.legend(loc='best', shadow=True, fontsize='9')
mag_plot.set(title='Grid connected test - PI + FF')
mag_plot.set(xlim=[0, 0.05], ylim=[-2, 2])
mag_plot.grid(True, which='minor', axis='both')
plt.savefig('HILxPSIM_comp.png', dpi=1000)
