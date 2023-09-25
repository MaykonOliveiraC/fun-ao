var = 7
def mudar_e_imprimir():
    global var
    var = 13
    print('Variavel dentro da função',var)

print('Variável antes de mudar',var)
mudar_e_imprimir()
print('variável depois de mudar',var)

var = 7
novo_valor = 13

def mudar_e_imprimir(novo_valor):
    global var
    var = novo_valor
    print('Variável dentro da função', var)

print('Variavel antes de mudar', var)
mudar_e_imprimir(novo_valor)