class Carro:
    def __init__(self, ano, modelo, km):
        self.ano = ano
        self.modelo = modelo
        self.km = km
    pass

    def AbrePorta(self):
        print('Abrindo a porta')

    
    def FecharPorta(self):
        print('Fechando porta')


    def LigarCarro(self):
        print('ligando carro')

    
    def infosCarro(self):
        print(self.ano, self.modelo, self.km)


Carro1 = Carro('2020', 'Sandero', '1000')
Carro1.AbrePorta()
Carro1.FecharPorta()
Carro1.LigarCarro()
Carro1.infosCarro()