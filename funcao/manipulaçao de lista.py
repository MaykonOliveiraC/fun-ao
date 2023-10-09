def ler_numeros():
    numeros = []
    for i in range(10):
        num = int(input(f'Digite o {i+1}º número: '))
        numeros.append(num)
    return numeros

def encontrar_maior(lista):
    maior = max(lista)
    return maior

def calcular_soma(lista):
    soma = sum(lista)
    return soma

def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

# Lendo os números
numeros = ler_numeros()

# Encontrando o maior número
maior = encontrar_maior(numeros)

# Calculando a soma
soma = calcular_soma(numeros)

# Calculando a média
media = calcular_media(numeros)

# Exibindo os resultados
print(f'O maior número é: {maior}')
print(f'A soma dos números é: {soma}')
print(f'A média dos números é: {media}')
