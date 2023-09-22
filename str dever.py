#Faça um programa que tenha uma função cchamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#Ex; escreva('Olá, Mundo!')
#Saída: ~~~~~~~~~~~
#       Olá, Mundo!
#       ~~~~~~~~~~~

def escreva(texto):
    tamanho = len(texto)
    linha = '-' * (tamanho + 4)
    
    print(linha)
    print(f'| {texto} |')
    print(linha)

mensagem = "Teste, teste, teste, teste"
escreva(mensagem)
