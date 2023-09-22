#Faça um programa que tenha uma função chamada área(), que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area():
    print('Controle de Terrenos\n--------------------')
    largura = float(input('Largura[m]: '))
    comprimento =  float(input('Comprimento[m]: '))
    area = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {area}. ')


area()