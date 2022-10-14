#Aluno: Pedro Henrique D M Santos
#Disciplina: Cálculo Numérico
#Método da Iteração Linear

from math import pow, sqrt, log
from sympy import diff, Symbol


def raizes(a, b, c):
    delta = pow(b, 2) - (4 * a * c)
    raiz1 = (-b + sqrt(delta)) / 2 * a
    raiz2 = (-b - sqrt(delta)) / 2 * a
    return raiz1, raiz2


def pontoValido(raiz1, raiz2):
    eq1_x1 = sqrt(raiz1 + 6)
    eq1_x2 = sqrt(raiz2 + 6)
    eq2_x1 = pow(raiz1, 2) - 6
    eq2_x2 = pow(raiz2, 2) - 6
    eq3_x1 = 1 + (6 / raiz1)
    eq3_x2 = 1 + (6 / raiz2)
    eqs = [ (eq1_x1, eq1_x2), (eq2_x1, eq2_x2), (eq3_x1, eq3_x2)]
    frases = ["Para a equação x = √ x + 6: ", "Para a equação x = x² - 6: ", "Para a equação x = 1 + 6 / x"]
    contador = 0
    for eq in eqs:
        print(f"\n{frases[contador]}")
        if eq[0] == (raiz1):
            print(f"O ponto {raiz1} é válido!")
        else:
            print(f"O ponto {raiz1} não é válido!")
        if eq[1] == (raiz2):
            print(f"O ponto {raiz2} é válido!")
        else:
            print(f"O ponto {raiz2} não é válido!")
        contador = contador + 1


def analiseDeConvergencia(x1, x2):
    print("\nApós aplicar a derivada em cada equação e analisar a sua convergência, onde a fórmula utilizada foi: |f'(x)| < 1, obtemos:")
    x = Symbol('x')
    eq1 = (x + 6) ** (1 / 2)
    eq2 = x ** 2 - 6
    eq3 = 1 + (6 / x)
    contador = 0
    frases = ["Pra a equação x = √ x + 6: ", "Para a equação x = x² - 6: ", "Para a equação x = 1 + 6 / x"]
    eqs = [eq1, eq2, eq3]
    for i in eqs:
        derivada = i.diff(x)
        derivada = str(derivada)
        result_x1 = derivada.replace("x", str(x1))
        result_x1 = eval(result_x1)
        result_x1 = abs(result_x1)
        result_x2 = derivada.replace("x", str(x2))
        result_x2 = eval(result_x2)
        result_x2 = abs(result_x2)
        print(f"\n{frases[contador]}")
        if result_x1 < 1:
            print(f"O ponto {x1} é convergente!")
        else:
            print(f"O ponto {x1} é divergente!")

        if result_x2 < 1:
            print(f"O ponto {x2} é convergente!")
        else:
            print(f"O ponto {x2} é divergente!")
        contador = contador + 1


def ordemDeConvergencia(x1, x2):
    iteracoes = 7
    raizess = (x1, x2)
    print(f"\nPara a ordem de convergência serão utilizdas as raízes {x1} e {x2} e feitas {iteracoes} iterações.")
    xks = [3.5, -1.5]
    print("\nPara a equação x = √ x + 6")
    for i in range(2):
        eks = ["ek-1", "ek", "ek+1"]
        print(f"\nPara a raiz {raizess[i]} e chute inicial de {xks[i]}, temos: ")
        print("K     X     ek   P")
        for k in range(iteracoes):
            ek = xks[i] - raizess[i]
            eks.pop(0)
            eks.insert(2, ek)
            if "ek+1" not in eks:
                  p = (log(eks[2] / eks[1])) / (log(eks[1] / eks[0]))
            else:
                 p = "--"
            print(f"{k}  {xks[i]:.5f}  {ek:.5f}   {p}")
            xks[i] = sqrt(xks[i] + 6)


def main():
    x1, x2 = raizes(1, -1, -6)
    print(f"Raízes da equação f(x) = x² - x - 6: ({x1}) e ({x2})")
    print("Equações de ponto fixo:\n  x = raiz(x+6);\n  x = x² - 6;\n  x = 1 + 6/x")
    pontoValido(x1, x2)
    analiseDeConvergencia(x1, x2)
    ordemDeConvergencia(x1, x2)


main()