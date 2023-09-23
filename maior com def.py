def maior(*valores):
    maior_valor = 0
    for numero in valores:
        if numero > maior_valor:
            maior_valor = numero
    print(f'O maior valor é entre {valores} é {maior_valor}.')


maior(15, 25, 245, 799, 866)
maior(1, 2, 15, 560)


