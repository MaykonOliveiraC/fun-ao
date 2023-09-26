def voto():
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    idade = 2023 - ano_nascimento
    if idade >= 18 and idade < 70:
        print(f'Você vota de forma obrigatória.')
    elif idade >= 70:
        print(f"Você tem voto opcional.")
    else:
        print(f"Você não possui idade para votar.")

   
 

voto()