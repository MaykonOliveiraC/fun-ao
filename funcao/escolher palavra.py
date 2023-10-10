import random

def escolher_palavra():
    palavras = ["python", "javascript", "java", "ruby", "html", "css"]
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_erradas = []
    letras_corretas = []
    tentativas = 6

    while tentativas > 0:
        palavra_mascarada = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_mascarada += letra
            else:
                palavra_mascarada += "_"

        print(f"Palavra: {palavra_mascarada}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        if palavra_mascarada == palavra:
            print("Parabéns! Você acertou a palavra!")
            return

        palpite = input("Digite uma letra ou a palavra completa: ").lower()

        if len(palpite) == 1:
            if palpite in palavra:
                letras_corretas.append(palpite)
            else:
                letras_erradas.append(palpite)
                tentativas -= 1
        elif len(palpite) == len(palavra) and palpite == palavra:
            print("Parabéns! Você acertou a palavra!")
            return
        else:
            print("Palpite inválido!")

    print(f"Você perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    print("Bem-vindo ao jogo da forca!")
    jogar_forca()
