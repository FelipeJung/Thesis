

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
R_L1 = 0.04     # Measured resistance at 0 Hz
# R_L1 = 0.05   # Measured resistance at 2.5 kHz
R_l2 = 0.58     # Measured resistance at 0 Hz
# R_l2 = 7.8    # Measured resistance at 2.5 kHz

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


Z_L1 = control.tf([L1, R_L1], [1])
Z_L2 = control.tf([L2, R_l2], [1])
Z_C1 = control.tf([1], [C1, 1])
Z_Cd = control.tf([1], [Rd*Cd, 1])
Z_C = control.tf([Cd*Rd, 1], [C1*Cd*Rd, Cd+C1, 0])

G_id = v_bus*Z_C/(Z_L1*Z_C + Z_C*Z_L2 + Z_L1*Z_L2)
omega = [(x*10)+63 for x in range(15915)]
mag1, phase1, omega1 = control.bode_plot(G_id, omega=omega, dB=True, Hz=True, deg=True, Plot=True, c='m', lineWidth=3)
mag2, phase2, omega2 = control.bode_plot(sys, omega=omega, dB=True, Hz=True, deg=True, Plot=True, c='k')
plt.close()

# Gráficos da comparação entre o sistema modelado e os resultados da ferramenta ACSweep do PSIM
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
mag_plot.set(title='Comparison between ideal and non-ideal transfer function')
mag_plot.set(xlim=[10, 25000], ylim=[-10, 75])
phase_plot.set(xlim=[10, 25000], ylim=[-280, 0])
mag_plot.grid(True, which='minor', axis='both')
omega = [((x*10)+63)/6.28 for x in range(15915)]

mag_plot.plot(omega, 20 * np.log10(mag1), c='r', lineWidth=3, label='With Inductor´s Resistance')
mag_plot.plot(omega, 20*np.log10(mag2), ':', c='black', lineWidth=2, label='Without Inductor´s Resistance')
phase_plot.plot(omega, phase1*180/3.14, c='r', lineWidth=3)
phase_plot.plot(omega, phase2*180/3.14, ':', c='black', lineWidth=2)

legend = mag_plot.legend(loc='best', shadow=True, fontsize='9')

plt.tight_layout()
plt.savefig('comparacao_bode_apendice.png', dpi=2000)
# plt.show()
