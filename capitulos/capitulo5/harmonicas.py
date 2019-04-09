
import matplotlib.pyplot as plt
import pandas
import numpy as np

plt.rcParams["font.family"] = 'Times New Roman'
plt.rcParams["font.style"] = 'normal'
plt.rcParams["font.variant"] = 'normal'
plt.rcParams["font.weight"] = 'normal'
plt.rcParams["font.stretch"] = 'normal'
plt.rcParams["font.size"] = '11'

plt.figure()
plt.ylabel("Amplitude (%)")
plt.xlabel("Harmonic Nbr")
harmonicas = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/testes_experimentais/Harmonicas.csv",  sep='\t')
width = 4/5
std_harm = np.arange(2, 31)
std_amp = np.array([1, 4, 1, 4, 1, 4, 1, 4, 0.5, 2, 0.5, 2, 0.5, 2, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5,
                    0.6, 0.5, 0.6, 0.5, 0.6, 0.5, 0.6, 0.5])

plt.bar(std_harm, std_amp, width, label='Standard', color='0.75')
plt.plot(harmonicas["Harmonic"], harmonicas["PI"], 'o:', label='PI', color='k')
plt.plot(harmonicas["Harmonic"], harmonicas["PR"], 'o:', label='PR', color='m')
plt.plot(harmonicas["Harmonic"], harmonicas["Rep"], 'o:', label='Rep', color='r')
plt.plot(harmonicas["Harmonic"], harmonicas["PIMR2"], 'o-', label='PI+MR 15h', color='g', LineWidth=3)

legend = plt.legend(loc='best', shadow=True, fontsize='9')
#plt.set(title='Control without feedforward - Harmonics')
plt.tight_layout()




plt.figure()
plt.ylabel("Amplitude (%)")
plt.xlabel("Harmonic Nbr")

plt.bar(std_harm, std_amp, width, label='Standard', color='0.75')
plt.plot(harmonicas["Harmonic"], harmonicas["Prop+FF"], 'o:', label='Prop + FF', color='b')
plt.plot(harmonicas["Harmonic"], harmonicas["PI+FF"], 'o:', label='PI + FF', color='g')
plt.plot(harmonicas["Harmonic"], harmonicas["MR+FF"], 'o:', label='MR + FF', color='r')
plt.plot(harmonicas["Harmonic"], harmonicas["PR+FF"], 'o:', label='PR + FF', color='c')
plt.plot(harmonicas["Harmonic"], harmonicas["Rep+FF"], 'o:', label='Rep + FF', color='m')
plt.plot(harmonicas["Harmonic"], harmonicas["PIMR2+FF"], 'o-', label='PI+MR 15h', color='y', LineWidth=3)
plt.plot(harmonicas["Harmonic"], harmonicas["PIMR+FF"], 'o:', label='PI+MR 10h odd', color='k')

legend = plt.legend(loc='best', shadow=True, fontsize='9')
#plt.set(title='Control without feedforward - Harmonics')
plt.tight_layout()
plt.show()