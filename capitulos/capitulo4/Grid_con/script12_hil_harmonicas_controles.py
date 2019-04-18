
import matplotlib.pyplot as plt
import pandas
import numpy as np
import math

plt.rcParams["font.family"] = 'Times New Roman'
plt.rcParams["font.style"] = 'normal'
plt.rcParams["font.variant"] = 'normal'
plt.rcParams["font.weight"] = 'normal'
plt.rcParams["font.stretch"] = 'normal'
plt.rcParams["font.size"] = '11'

col_names = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17', 'a18', 'a19', 'thd_i']
harmonicas_pi = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo4/grid_con/PI_harmonicas.csv", sep=',', header=None, names=col_names)
harmonicas_pr = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo4/grid_con/PR_harmonicas.csv", sep=',', header=None, names=col_names)
harmonicas_mr = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo4/grid_con/MR_harmonicas.csv", sep=',', header=None, names=col_names)
harmonicas_rep = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo4/grid_con/Rep_harmonicas.csv", sep=',', header=None, names=col_names)
# harmonicas_prop = pandas.read_csv("D:/Users/FELIPE/Documents/Mestrado/dissertacao/capitulos/Capitulo4/grid_con/Prop_harmonicas.csv", sep=',', header=None, names=col_names)


#
# thd_prop = np.mean(np.array(harmonicas_prop['thd_i']))
# a1_prop = np.mean(np.array(harmonicas_prop['a0']))
# a2_prop = np.mean(np.array(harmonicas_prop['a1']))
# a3_prop = np.mean(np.array(harmonicas_prop['a2']))
# a4_prop = np.mean(np.array(harmonicas_prop['a3']))
# a5_prop = np.mean(np.array(harmonicas_prop['a4']))
# a6_prop = np.mean(np.array(harmonicas_prop['a5']))
# a7_prop = np.mean(np.array(harmonicas_prop['a6']))
# a8_prop = np.mean(np.array(harmonicas_prop['a7']))
# a9_prop = np.mean(np.array(harmonicas_prop['a8']))
# a10_prop = np.mean(np.array(harmonicas_prop['a9']))
# a11_prop = np.mean(np.array(harmonicas_prop['a10']))
# a12_prop = np.mean(np.array(harmonicas_prop['a11']))
# a13_prop = np.mean(np.array(harmonicas_prop['a12']))
# a14_prop = np.mean(np.array(harmonicas_prop['a13']))
# a15_prop = np.mean(np.array(harmonicas_prop['a14']))
# a16_prop = np.mean(np.array(harmonicas_prop['a15']))
# a17_prop = np.mean(np.array(harmonicas_prop['a16']))
# a18_prop = np.mean(np.array(harmonicas_prop['a17']))
# a19_prop = np.mean(np.array(harmonicas_prop['a18']))
# a20_prop = np.mean(np.array(harmonicas_prop['a19']))
# prop = [a2_prop, a3_prop, a4_prop, a5_prop, a6_prop, a7_prop, a8_prop, a9_prop, a10_prop, a11_prop,
#                         a12_prop, a13_prop, a14_prop, a15_prop, a16_prop, a17_prop, a18_prop, a19_prop, a20_prop]
# prop = [100*a/a1_prop for a in prop]



thd_pi = np.mean(np.array(harmonicas_pi['thd_i']))
a1_pi = np.mean(np.array(harmonicas_pi['a0']))
a2_pi = np.mean(np.array(harmonicas_pi['a1']))
a3_pi = np.mean(np.array(harmonicas_pi['a2']))
a4_pi = np.mean(np.array(harmonicas_pi['a3']))
a5_pi = np.mean(np.array(harmonicas_pi['a4']))
a6_pi = np.mean(np.array(harmonicas_pi['a5']))
a7_pi = np.mean(np.array(harmonicas_pi['a6']))
a8_pi = np.mean(np.array(harmonicas_pi['a7']))
a9_pi = np.mean(np.array(harmonicas_pi['a8']))
a10_pi = np.mean(np.array(harmonicas_pi['a9']))
a11_pi = np.mean(np.array(harmonicas_pi['a10']))
a12_pi = np.mean(np.array(harmonicas_pi['a11']))
a13_pi = np.mean(np.array(harmonicas_pi['a12']))
a14_pi = np.mean(np.array(harmonicas_pi['a13']))
a15_pi = np.mean(np.array(harmonicas_pi['a14']))
a16_pi = np.mean(np.array(harmonicas_pi['a15']))
a17_pi = np.mean(np.array(harmonicas_pi['a16']))
a18_pi = np.mean(np.array(harmonicas_pi['a17']))
a19_pi = np.mean(np.array(harmonicas_pi['a18']))
a20_pi = np.mean(np.array(harmonicas_pi['a19']))
pi = [a2_pi, a3_pi, a4_pi, a5_pi, a6_pi, a7_pi, a8_pi, a9_pi, a10_pi, a11_pi,
                        a12_pi, a13_pi, a14_pi, a15_pi, a16_pi, a17_pi, a18_pi, a19_pi, a20_pi]
pi = [100*a/a1_pi for a in pi]



thd_pr = np.mean(np.array(harmonicas_pr['thd_i']))
a1_pr = np.mean(np.array(harmonicas_pr['a0']))
a2_pr = np.mean(np.array(harmonicas_pr['a1']))
a3_pr = np.mean(np.array(harmonicas_pr['a2']))
a4_pr = np.mean(np.array(harmonicas_pr['a3']))
a5_pr = np.mean(np.array(harmonicas_pr['a4']))
a6_pr = np.mean(np.array(harmonicas_pr['a5']))
a7_pr = np.mean(np.array(harmonicas_pr['a6']))
a8_pr = np.mean(np.array(harmonicas_pr['a7']))
a9_pr = np.mean(np.array(harmonicas_pr['a8']))
a10_pr = np.mean(np.array(harmonicas_pr['a9']))
a11_pr = np.mean(np.array(harmonicas_pr['a10']))
a12_pr = np.mean(np.array(harmonicas_pr['a11']))
a13_pr = np.mean(np.array(harmonicas_pr['a12']))
a14_pr = np.mean(np.array(harmonicas_pr['a13']))
a15_pr = np.mean(np.array(harmonicas_pr['a14']))
a16_pr = np.mean(np.array(harmonicas_pr['a15']))
a17_pr = np.mean(np.array(harmonicas_pr['a16']))
a18_pr = np.mean(np.array(harmonicas_pr['a17']))
a19_pr = np.mean(np.array(harmonicas_pr['a18']))
a20_pr = np.mean(np.array(harmonicas_pr['a19']))
pr = [a2_pr, a3_pr, a4_pr, a5_pr, a6_pr, a7_pr, a8_pr, a9_pr, a10_pr, a11_pr,
                        a12_pr, a13_pr, a14_pr, a15_pr, a16_pr, a17_pr, a18_pr, a19_pr, a20_pr]
pr = [100*a/a1_pr for a in pr]



thd_mr = np.mean(np.array(harmonicas_mr['thd_i']))
a1_mr = np.mean(np.array(harmonicas_mr['a0']))
a2_mr = np.mean(np.array(harmonicas_mr['a1']))
a3_mr = np.mean(np.array(harmonicas_mr['a2']))
a4_mr = np.mean(np.array(harmonicas_mr['a3']))
a5_mr = np.mean(np.array(harmonicas_mr['a4']))
a6_mr = np.mean(np.array(harmonicas_mr['a5']))
a7_mr = np.mean(np.array(harmonicas_mr['a6']))
a8_mr = np.mean(np.array(harmonicas_mr['a7']))
a9_mr = np.mean(np.array(harmonicas_mr['a8']))
a10_mr = np.mean(np.array(harmonicas_mr['a9']))
a11_mr = np.mean(np.array(harmonicas_mr['a10']))
a12_mr = np.mean(np.array(harmonicas_mr['a11']))
a13_mr = np.mean(np.array(harmonicas_mr['a12']))
a14_mr = np.mean(np.array(harmonicas_mr['a13']))
a15_mr = np.mean(np.array(harmonicas_mr['a14']))
a16_mr = np.mean(np.array(harmonicas_mr['a15']))
a17_mr = np.mean(np.array(harmonicas_mr['a16']))
a18_mr = np.mean(np.array(harmonicas_mr['a17']))
a19_mr = np.mean(np.array(harmonicas_mr['a18']))
a20_mr = np.mean(np.array(harmonicas_mr['a19']))
mr = [a2_mr, a3_mr, a4_mr, a5_mr, a6_mr, a7_mr, a8_mr, a9_mr, a10_mr, a11_mr,
        a12_mr, a13_mr, a14_mr, a15_mr, a16_mr, a17_mr, a18_mr, a19_mr, a20_mr]
mr = [100*a/a1_mr for a in mr]




thd_rep = np.mean(np.array(harmonicas_rep['thd_i']))
a1_rep = np.mean(np.array(harmonicas_rep['a0']))
a2_rep = np.mean(np.array(harmonicas_rep['a1']))
a3_rep = np.mean(np.array(harmonicas_rep['a2']))
a4_rep = np.mean(np.array(harmonicas_rep['a3']))
a5_rep = np.mean(np.array(harmonicas_rep['a4']))
a6_rep = np.mean(np.array(harmonicas_rep['a5']))
a7_rep = np.mean(np.array(harmonicas_rep['a6']))
a8_rep = np.mean(np.array(harmonicas_rep['a7']))
a9_rep = np.mean(np.array(harmonicas_rep['a8']))
a10_rep = np.mean(np.array(harmonicas_rep['a9']))
a11_rep = np.mean(np.array(harmonicas_rep['a10']))
a12_rep = np.mean(np.array(harmonicas_rep['a11']))
a13_rep = np.mean(np.array(harmonicas_rep['a12']))
a14_rep = np.mean(np.array(harmonicas_rep['a13']))
a15_rep = np.mean(np.array(harmonicas_rep['a14']))
a16_rep = np.mean(np.array(harmonicas_rep['a15']))
a17_rep = np.mean(np.array(harmonicas_rep['a16']))
a18_rep = np.mean(np.array(harmonicas_rep['a17']))
a19_rep = np.mean(np.array(harmonicas_rep['a18']))
a20_rep = np.mean(np.array(harmonicas_rep['a19']))
rep = [a2_rep, a3_rep, a4_rep, a5_rep, a6_rep, a7_rep, a8_rep, a9_rep, a10_rep, a11_rep,
        a12_rep, a13_rep, a14_rep, a15_rep, a16_rep, a17_rep, a18_rep, a19_rep, a20_rep]
rep = [100*a/a1_rep for a in rep]


std_harm = np.arange(2, 21)
std_amp = np.array([1, 4, 1, 4, 1, 4, 1, 4, 0.5, 2, 0.5, 2, 0.5, 2, 0.5, 1.5, 0.5, 1.5, 0.5])


fig = plt.figure()
harm = fig.add_subplot(111)
plt.ylabel("Amplitude (%)")
plt.xlabel("Harmonic Nbr")
width = 0.8
plt.plot(std_harm, pi, 'o:', label='PI', color='m')
plt.plot(std_harm, pr, 'o:', label='PR', color='r')
plt.plot(std_harm, rep, 'o:', label='Rep', color='b')
plt.plot(std_harm, mr, 'o-', label='PI+MR 15h', color='g', LineWidth=3)
plt.bar(std_harm, std_amp, width, label='Standard', color='0.75', alpha=0.5)
legend = plt.legend(loc='best', shadow=True, fontsize='9')
harm.set(title='Control without feedforward - Harmonics', xlim=[1, 15.5], ylim=[0, 4.2])
plt.savefig('Harm_FF.png', dpi=1000)

std_harm = [h for h in std_harm]
std_amp = [h for h in std_amp]
std_harm.pop(0)
std_amp.pop(0)
pi.pop(0)
pr.pop(0)
mr.pop(0)
rep.pop(0)


fig = plt.figure()
harm = fig.add_subplot(111)
plt.ylabel("Amplitude (%)")
plt.xlabel("Harmonic Nbr")
width = 0.8
plt.plot(std_harm, pi, 'o:', label='PI', color='m')
plt.plot(std_harm, pr, 'o:', label='PR', color='r')
plt.plot(std_harm, rep, 'o:', label='Rep', color='b')
plt.plot(std_harm, mr, 'o-', label='PI+MR 15h', color='g', LineWidth=3)
plt.bar(std_harm, std_amp, width, label='Standard', color='0.75', alpha=0.5)
legend = plt.legend(loc='best', shadow=True, fontsize='9')
harm.set(title='Control without feedforward - Harmonics', xlim=[2.5, 15.5], ylim=[0, 0.05])
plt.savefig('Harm_FF_zoom.png', dpi=1000)

# THD_soma = 0
# for k in prop:
#     THD_soma += k*k/10000
# THD_p = 100*math.sqrt(THD_soma)
#
# print(THD_p, thd_prop)