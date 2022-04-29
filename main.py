import matplotlib.pyplot as plt
import numpy as np

'''
Columns
(0) - Survival time
(5) - EPSS
(6) - LVDD
'''

# Primeira Análise
# H_0 -> não morre no es
# paço de 1 ano após o ataque cardiaco (S >= 12 meses)
# H_A -> morre no espaço de 1 ano após o ataque cardiaco (S < 12 meses)

# Segunda Análise
# Dado que a pessoa teve um ataque cardiaco, qual a probabilidade que tendo um LVDD baixo e um EPSS alto que ela tenha ataque cardiaco
# LVDD anormal -> 5.9 <= x < 6.8 (https://www.techmed.sk/en/echo/normal-values/)

https://github.com/Mathbonc/Projeto_Estatistica2021_2.git