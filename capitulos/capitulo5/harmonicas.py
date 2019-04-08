
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

plt.bar(std_harm, std_amp, width, label='Standard')
plt.plot(harmonicas["Harmonic"], harmonicas["PI"], label='PI', color='k')
plt.plot(harmonicas["Harmonic"], harmonicas["PR"], label='PR', color='m')
plt.plot(harmonicas["Harmonic"], harmonicas["Rep"], label='Rep', color='r')
plt.plot(harmonicas["Harmonic"], harmonicas["PIMR2"], label='PI+MR 15h', color='g')

#plt.bar(harmonicas["Harmonic"], harmonicas["PI"], 0.35)
legend = plt.legend(loc='best', shadow=True, fontsize='9')
#plt.set(title='Control without feedforward - Harmonics')
plt.tight_layout()
plt.show()