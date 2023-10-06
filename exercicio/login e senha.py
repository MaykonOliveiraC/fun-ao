login_secreto = "mk"
senha_secreta = "123"

login = input("Digite o seu login: ")
if (login == login_secreto):
    senha = input("Digita a senha: ")
    if (senha == senha_secreta):
        print("Bem vindo ao sistema")
        print("Sua conta corrente tem R$100")
    else:
        print("Combinação de senha e login incorretos")
else:
    print("Login não existe na base de dados.")