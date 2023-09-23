import random

def sortear_numeros():
    numeros_sorteados = []
    for _ in range(5):
        numeros_sorteados.append(random.randint(1, 100))
    print(f"Os números sorteados são: {numeros_sorteados}")
    return numeros_sorteados


def somaPar(numeros_sorteados):
    pares = []
    for numero in numeros_sorteados:
        if numero % 2 == 0:
            pares.append(numero)
    soma = sum(pares)
    print(f' A soma dos numeros pares que são {pares} resultam em {soma}.')

numeros_sorteio = sortear_numeros()
somaPar(numeros_sorteio)
        

            


