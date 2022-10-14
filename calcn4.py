#Aluno: Pedro Henrique D M Santos
#Disciplina: Cálculo Numérico
#Método da Secante

from math import *


def calculaFunc(p1, p2):
    return p2 - (((4 * cos(p2) - pow(e, p2)) * (p1 * p2)) / ((4 * cos(p1) - pow(e, p1)) - (4 * cos(p2) - pow(e, p2))))


def calculaErro(p1, p2):
    return p2 - calculaFunc(p1, p2)


def main():
    num1 = 1.1
    num2 = 1
    aux = 0
    print("Valores iniciais dos pontos:")
    print("p0 = 1.1")
    print("p1 = 1")
    for x in range(3):
        print(f"\n\nIteração {x+1}:")
        print(f"p{x+2} = {calculaFunc(num1, num2)}")
        print(f"Erro absoluto {x+1} = {calculaErro(num1, num2)}")
        aux = num2
        num2 = calculaFunc(num1, num2)
        num1 = aux


main()
