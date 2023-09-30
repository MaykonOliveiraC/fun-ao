import random

class NumerosAleatorios:
    def __init__(self, minimo, maximo):
        self.minimo = minimo
        self.maximo = maximo

    def gerar_numero(self):
        return random.randint(self.minimo, self.maximo)


class NomesAleatorios:
    def __init__(self, lista_nomes):
        self.lista_nomes = lista_nomes

    def gerar_nome(self):
        return random.choice(self.lista_nomes)


class CoresAleatorias:
    def __init__(self, lista_cores):
        self.lista_cores = lista_cores

    def gerar_cor(self):
        return random.choice(self.lista_cores)


# Exemplo de uso
numeros = NumerosAleatorios(1, 10)
print("Número aleatório:", numeros.gerar_numero())

nomes = NomesAleatorios(["Alice", "Bob", "Charlie", "David"])
print("Nome aleatório:", nomes.gerar_nome())

cores = CoresAleatorias(["vermelho", "verde", "azul", "amarelo"])
print("Cor aleatória:", cores.gerar_cor())
