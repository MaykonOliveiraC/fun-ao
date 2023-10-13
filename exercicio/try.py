try:
    num = int(input("Digite um número: "))
    resultado = 10 / num
    print("O resultado é:", resultado)
except ValueError as ve:
    print("Erro: Valor inválido. Por favor, digite um número.")
except ZeroDivisionError as ze:
    print("Erro: Divisão por zero.")
else:
    print("Nenhum erro ocorreu.")
finally:
    print("Finalizando o bloco try-except.")
