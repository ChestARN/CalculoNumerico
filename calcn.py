#Aluno: Pedro Henrique D M Santos
#Disciplina: Cálculo Numérico

import math

a = 1
b = 2
e = 0.01
k = math.ceil((math.log(b - a,10) - math.log(e, 10))/math.log(2, 10))
cont = 0
x0 = (a + b)/2
sin = '+'
formula1 = math.pow(a, 2) - 3
formula2 = math.pow(x0, 2) - 3
e = b - a
print(f'|{cont}|{a:.2f}|{b:.2f}|{x0:.2f}|{formula1:.2f}|{formula2:.2f}|{sin}|{e:.3f}|')

while cont <= k:
    formula1 = math.pow(a, 2) - 3
    formula2 = math.pow(x0, 2) - 3
    if (formula1 * formula2) > 0:
        a = x0
        x0 = (a + b)/2
        sin = '+'
    else:
        b = x0
        x0 = (a + b)/2
        sin = '-'
    cont = cont + 1
    e = b - a
    print(f'|{cont}|{a:.2f}|{b:.2f}|{x0:.2f}|{formula1:.2f}|{formula2:.2f}|{sin}|{e:.3f}|')
