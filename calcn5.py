#Aluno: Pedro Henrique D M Santos
#Disciplina: Cálculo Numérico
#Método de Gauss-Seidel

from math import *

def main():
    x = [1, 1, 1]
    cont = 0
    while cont < 7:
        print(f'x{cont+1}: ', x)
        retornaFunc(x)
        cont = cont + 1

def retornaFunc(lista):
    lista[0] =( (lista[0]/3) + (lista[1]/3) + 2 ).__round__(2)
    lista[1] = (-0.4*lista[0] - 0.1*lista[2] + 2.3).__round__(2)
    lista[2] = ((-0.25*lista[0]) + (0.25*lista[1]) - 1.25).__round__(2)

main()
