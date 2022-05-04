from statistics import pstdev
from traceback import print_tb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import utils as uts
from scipy.stats import ttest_1samp
from scipy.stats import geom


data_file = open('./echocardiogram.data', 'r')
file_lines = data_file.readlines() # le as linhas e as guarda em uma lista
clearedData = []

# Processing the data
for lineIndex in range(len(file_lines)):
    line = file_lines[lineIndex].split(',')

    line[0] = uts.parseToNum(line[0])
    line[1] = uts.parseToNum(line[1])
    line[5] = uts.parseToNum(line[5])
    line[6] = uts.parseToNum(line[6])

    clearedData.append([line[0], line[1], line[5], line[6]])


# Primeira Análise ===============================================================
# H_0 -> Uma pessoa irá morrer dentro de 12 meses após o primeiro ataque (S < =12 meses)
# H_A -> A pessoa sobrevive mais de um ano (S > 12 meses)
#  - Nível se significância (a) = 0.05
#  - Calcular Sigma
#  - Estatistica de teste z
#  - Area que correponde a z
#  - Encontrar valor p (Rejeita p<= a)

survivalTimes = []
critValue = 1.660 #Região crítica tabelado com base no grau de liberdade (100+)
a = b = c = 0

for line in clearedData:
    if line[0]:
        if line[0]>=12:
            a = a + 1 
        else:
            b = b + 1  
        survivalTimes.append(line[0]) #Limpando ainda mais o array (Retirando os "None"'s)
        if line[0]<=1.04732143:
            c = c + 1

#Fazendo o teste de hipoteses
test, pval = ttest_1samp(survivalTimes, 12, alternative='greater')

if(pval<=0.05):
    print('A hipotese nula foi rejeitada')
else:
    print('Nao ha evidencias suficientes para negar a hipotese nula')

#Tentativa de plot
#Utilizando uma distribuição Binomial, com base em diversas provas de Bernoulli
fig, ax = plt.subplots()
fig2, axx = plt.subplots()


#print(np.floor(max(survivalTimes)))

bin_edges = np.linspace(min(survivalTimes), max(survivalTimes), num=57, endpoint=True)
count, bins, ignored = ax.hist(survivalTimes, bin_edges, density= False)

Curva = pd.DataFrame(survivalTimes)
Curva.agg(['min', 'max', 'mean', 'std']).round(decimals=2)
Curva.plot.kde(ax=axx, legend=False, title='Months survived after first heart attack (KDE)')
Curva.plot.hist(density=True, ax=axx)

ax.grid(axis='y', alpha=0.75) 
axx.grid(axis='y', alpha=0.75)
ax.text(3.24,23.0, 'y = 23')

ax.set_ylabel('Patients')
ax.set_xlabel('Months Survived')
ax.set_title('Months survived after first heart attack (KDE)')
ax.set_facecolor('#D6CFC7')
axx.set_ylabel('Patients')
axx.set_xlabel('Months Survived')
axx.set_facecolor('#D6CFC7')

plt.show()

# Segunda Análise ===============================================================
# Dado que a pessoa teve um ataque cardiaco, qual a probabilidade que tendo um LVDD baixo e um EPSS alto que ela tenha ataque cardiaco
# LVDD anormal -> 5.9 <= x < 6.8 (https://www.techmed.sk/en/echo/normal-values/)

# 1. Calcular quantas pessoas tem EPSS alto e LVDD no range citado
