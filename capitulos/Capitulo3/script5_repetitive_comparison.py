
import control
import matplotlib.pyplot as plt
import pandas
import numpy as np
from control.matlab import *
plt.rcParams["font.family"] = 'Times New Roman'
plt.rcParams["font.style"] = 'normal'
plt.rcParams["font.variant"] = 'normal'
plt.rcParams["font.weight"] = 'normal'
plt.rcParams["font.stretch"] = 'normal'
plt.rcParams["font.size"] = '11'

fig = plt.figure()
mag_plot = fig.add_subplot(211)
plt.xscale('log')
plt.ylabel("Magnitude (dB)")
plt.grid(True)
phase_plot = fig.add_subplot(212)
phase_plot.grid(True, which='both', axis='both')
plt.xscale('log')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (deg)")
comp = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo3/Comp_rep_gain_variation.csv")
mag_plot.plot(comp["w"]*0.15915494, comp["g1"], ':', c='black', lineWidth=1, label='cr = 1')
mag_plot.plot(comp["w"]*0.15915494, comp["g2"], '-', c='r', lineWidth=1, label='cr = 0.6')
mag_plot.plot(comp["w"]*0.15915494, comp["g3"], '-.', c='g', lineWidth=1, label='cr = 0.1')
phase_plot.plot(comp["w"]*0.15915494, comp["f1"], ':', c='black', lineWidth=1)
phase_plot.plot(comp["w"]*0.15915494, comp["f2"], '-', c='r', lineWidth=1)
phase_plot.plot(comp["w"]*0.15915494, comp["f3"], '-.', c='g', lineWidth=1)
legend = mag_plot.legend(loc='best', shadow=True, fontsize='9')
mag_plot.set(title='Repetitive Control - gain variation')
mag_plot.set(xlim=[100*0.15915494, 50000*0.15915494], ylim=[-15, 75])
phase_plot.set(xlim=[100*0.15915494, 50000*0.15915494], ylim=[-100, 100])
mag_plot.grid(True, which='minor', axis='both')
plt.savefig('rep_gain_variation.png', dpi=2000)
plt.tight_layout()

fig = plt.figure()
mag_plot = fig.add_subplot(211)
plt.xscale('log')
plt.ylabel("Magnitude (dB)")
plt.grid(True)
phase_plot = fig.add_subplot(212)
phase_plot.grid(True, which='both', axis='both')
plt.xscale('log')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (deg)")
FTMA = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo3/FTMA.csv")
mag_plot.plot(FTMA["w"]*0.15915494, 20*np.log10(FTMA["g1"]), c='blue', lineWidth=1)
phase_plot.plot(FTMA["w"]*0.15915494, FTMA["f1"], c='blue', lineWidth=1)
legend = mag_plot.legend(loc='best', shadow=True, fontsize='9')
mag_plot.set(title='Bode diagram of the open-loop repetitive-control system')
mag_plot.set(xlim=[100*0.15915494, 100000*0.15915494], ylim=[-20, 40])
phase_plot.set(xlim=[100*0.15915494, 100000*0.15915494], ylim=[-270, 45])
mag_plot.grid(True, which='minor', axis='both')
plt.savefig('rep_gain_variation.png', dpi=2000)
plt.tight_layout()
plt.show()
