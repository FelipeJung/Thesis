

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

# diagrama de Nyquist
fig = plt.figure()

num = [0.5]
den = [1, 0.5, 1, 0]
system = tf(num, den)
w1 = np.linspace(0.11, 10, 1000)
w2 = np.linspace(0.14, 10, 1000)
w3 = np.linspace(0.17, 10, 1000)
print(system)
[re1, Im1, freq1] = control.nyquist_plot(system, w2, label="Unitary")
[re2, Im2, freq2] = control.nyquist_plot(0.8*system, w1, color='r', label="Small gain")
[re3, Im3, freq3] = control.nyquist_plot(1.2*system, w3, color='k', label="Large gain")
plt.clf()
plt.close()

fig = plt.figure()
fig = fig.add_subplot(111)
fig.set(title='Nyquist Plot')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.grid(True)
# ph = fig.add_subplot(212)
fig.grid(True, which='minor', axis='both')
#
fig.plot(re2, Im2, c='red', lineWidth=1, label="Small gain")
fig.plot(re1, Im1, c='black', lineWidth=2, label="Unitary")
fig.plot(re3, Im3, c='blue', lineWidth=3, label="Large gain")
fig.plot(-1, 0, marker='o')
plt.text(-1, -0.25, "-1 + j0")
legend = plt.legend(loc='best', shadow=True, fontsize='9')
a = '\\frac{5}{(s+1)(s+2)(s+3)}'
plt.title('Nyquist Diagram')
plt.savefig('exemplo_nyquist.png', dpi=2000)

