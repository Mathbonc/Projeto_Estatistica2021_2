import matplotlib.pyplot as plt
import numpy as np
import utils as uts
from scipy.stats import ttest_1samp

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
# H_0 -> não morre no espaço de 1 ano após o ataque cardiaco (S >= 12 meses)
# H_A -> morre no espaço de 1 ano após o ataque cardiaco (S < 12 meses)
#  - Nível se significância (a) = 0.05
#  - Calcular Sigma
#  - Estatistica de teste z
#  - Area que correponde a z
#  - Encontrar valor p (Rejeita p<= a)

survivalTimes = []
critValue = 1.660
a = b = 0

for line in clearedData:
    if line[0]:
        if line[0]>=12:
            a = a+1
        else:
            b = b+1
        survivalTimes.append(line[0]) #Limpando ainda mais o array (Retirando os "None"'s)

#Percentagem de pessoas que viveram mais de 12 meses
H0percent = a/len(survivalTimes)
H1percent = 1 - H0percent

print(H0percent, H1percent)




# Segunda Análise ===============================================================
# Dado que a pessoa teve um ataque cardiaco, qual a probabilidade que tendo um LVDD baixo e um EPSS alto que ela tenha ataque cardiaco
# LVDD anormal -> 5.9 <= x < 6.8 (https://www.techmed.sk/en/echo/normal-values/)

# 1. Calcular quantas pessoas tem EPSS alto e LVDD no range citado
