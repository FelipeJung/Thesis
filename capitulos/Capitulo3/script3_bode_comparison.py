
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

# Exemplos de resposta em frequencia para fundamentação do capítulo 3 da dissertação
fig = plt.figure()

num = [0.01, 5]
den = [1, 1, 10, 1]
system = tf(num, den)
[mag, phase, w] = control.matlab.bode(system)
plt.clf()
plt.close()
fig = plt.figure()
gain = fig.add_subplot(211)
gain.set(title='Bode diagram')
plt.ylabel('Magnitude (dB)')
plt.xscale('log')
plt.grid(True)
# gain.plot(10, -50, marker='o')
ph = fig.add_subplot(212)
ph.grid(True, which='both', axis='both')
plt.xscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (deg)')
gain.grid(True, which='minor', axis='both')

gain.plot(w, 20 * np.log10(mag), c='black', lineWidth=2)
gain.plot([0.1109, 0.6], [10.78729593, 0], c='k', marker='o', linestyle=None)
gain.text(0.03, -10, "cutoff freq")
gain.text(0.25, -25, "crossover freq")

ph.plot(w, phase*180/3.14, c='black', lineWidth=2)
ph.plot(3.2, -180, c='k', marker='o')
plt.text(4, -180, "-180º")
gain.set(xlim=[0.01, 1000], ylim=[-160, 20])
ph.set(xlim=[0.01, 1000], ylim=[-280, 0])
plt.savefig('exemplo_bode.png', dpi=2000)
gm, pm, wg, wp = control.margin(system)
print(f'Margem de ganho: {gm}, margem de fase: {pm}, frequencia cruzamento ganho: {wg}, frequencia cruzamento fase: {wp}')

