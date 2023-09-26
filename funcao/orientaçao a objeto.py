class ControleRemoto:
    def __init__(self, cor, altura, profundidade,  largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o canal.")
        elif botao == "-":
            print("Diminuir o canal.")
        






controle_remoto = ControleRemoto("Preto", "10m", "2cm", "2cm")

print(controle_remoto.altura)
print(controle_remoto.largura)
controle_remoto.passar_canal("+")
controle_remoto.passar_canal("-")
