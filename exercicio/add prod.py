# Função para adicionar produtos e preços à lista
def adicionar_produto_e_preco(lista, produto, preco):
    lista.append((produto, preco))

# Função para imprimir os produtos e preços da lista
def imprimir_produtos_e_precos(lista):
    for produto, preco in lista:
        print(f"Produto: {produto}, Preço: R${preco}")

# Criar uma lista vazia para armazenar os produtos e preços
lista_produtos_precos = []

# Solicitar os produtos e preços ao usuário
produto1 = input("Digite o nome do primeiro produto: ")
preco1 = float(input("Digite o preço do primeiro produto: "))

produto2 = input("Digite o nome do segundo produto: ")
preco2 = float(input("Digite o preço do segundo produto: "))

# Adicionar os produtos e preços à lista
adicionar_produto_e_preco(lista_produtos_precos, produto1, preco1)
adicionar_produto_e_preco(lista_produtos_precos, produto2, preco2)

# Imprimir os produtos e preços
print("\nLista de Produtos e Preços:")
imprimir_produtos_e_precos(lista_produtos_precos)
