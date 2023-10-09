def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Erro: Não é possível calcular a raiz de um número negativo."

def resto_divisao(a, b):
    return a % b
