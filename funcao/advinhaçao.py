import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while True:
        tentativa = int(input("Digite o seu palpite: "))

        if tentativa < 1 or tentativa > 100:
            print("Por favor, digite um número entre 1 e 100.")
            continue

        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif tentativa < numero_secreto:
            print("O número secreto é maior. Tente novamente.")
        else:
            print("O número secreto é menor. Tente novamente.")

if __name__ == "__main__":
    jogo_adivinhacao()
