#Aluno: Pedro Henrique D M Santos
#Disciplina: Cálculo Numérico
#Método de Newton

from math import *


def calculaFunc(p):
    return p - ((4 * cos(p) - pow(e, p)) / (-4 * sin(p) - pow(e, p)))


def calculaErro(p):
    return p - calculaFunc(p)


def main():
    num = float(1)
    print("Valor inicial do ponto:")
    print("p0 = 1")
    for x in range(2):
        print(f"\n\nIteração {x + 1}:")
        print(f"p{x+1} = {calculaFunc(num)}")
        print(f"Erro absoluto {x+1} = {calculaErro(num)}")
        num = calculaFunc(num)


main()
