

import control
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from control.matlab import *
plt.rcParams["font.family"] = 'Times New Roman'
plt.rcParams["font.style"] = 'normal'
plt.rcParams["font.variant"] = 'normal'
plt.rcParams["font.weight"] = 'normal'
plt.rcParams["font.stretch"] = 'normal'
plt.rcParams["font.size"] = '11'


#levantamento da função de transferência do modelo do microinversor

v_bus = 420
v_rede = 220
f_c = 100000
f_rede = 60
p_out = 250
delta_v = 0.001
delta_i = 1.9

L1 = 0.00018
L2 = 0.0012
C1 = 0.000001
Cd = C1
Rd = 15
R_L1 = 0.04
# R_L1 = 0.05
R_l2 = 0.58
# R_l2 = 7.8

b1 = v_bus*Rd*Cd
b0 = v_bus
a4 = L1*L2*C1*Cd*Rd
a3 = L1*L2*(C1+Cd)
a2 = Cd*Rd*(L1+L2)
a1 = L1 + L2
a0 = 0

num = [b1, b0]
den = [a4, a3, a2, a1, a0]

sys = control.tf(num, den)
print(sys)

omega = [x+627 for x in range(314159)]
# Initialize a Figure
fig = plt.figure()
mag, phase, omega = control.bode_plot(sys, omega=omega, dB=True, Hz=True, deg=True, Plot=True, c='m')
# plt.xlabel("frequency (Hz)")
# plt.ylabel("phase (degrees)")
# fig2 = plt.figure()
# control.bode_plot(sys, omega=omega, dB=True, Hz=True, deg=True, Plot=True, lineWidth=2)
# plt.plot(omega, mag, c='m')
# plt.plot(omega, phase)
# plt.show(fig)
# plt.show(fig2)
plt.clf()
plt.close(fig)

fig = plt.figure()
mag_plot = fig.add_subplot(211)
mag_plot.plot(omega/(6.28), 20*np.log10(mag), c='r', lineWidth=3, label='Model transfer function')
plt.xscale('log')
plt.ylabel("Magnitude (dB)")
plt.grid(True)
phase_plot = fig.add_subplot(212)
phase_plot.grid(True, which='both', axis='both')
phase_plot.plot(omega/6.28, phase*180/3.14, c='r', lineWidth=3)
plt.xscale('log')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (deg)")
df = pd.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo2/psim.csv")
mag_plot.plot(df['Frequency'], df['amp(Vo1)'], ':', c='black', lineWidth=2, label='Simulated AC Sweep response')
phase_plot.plot(df['Frequency'], df['phase(Vo1)'], ':', c='black', lineWidth=2)
legend = mag_plot.legend(loc='best', shadow=True, fontsize='9')
mag_plot.set(title='Comparison between simulated and model transfer function')
mag_plot.set(xlim=[100, 50000], ylim=[-25, 55])
phase_plot.set(xlim=[100, 50000], ylim=[-300, -80])
mag_plot.grid(True, which='minor', axis='both')

plt.savefig('figura_capitulo2.png')
# plt.show()

plt.close()

