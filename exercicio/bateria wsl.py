#Faça um programa para decidir o vencedor de uma bateria da WSL
# SÓ AS 2 MAIORES NOTAS DE CADA SURFISTA CONTA
# A MAIOR SOMA DAS 2 NOTAS DIZ O VENCEDOR

italo = [9.2, 7, 8.6, 6.7]
medina = [9.1, 8, 9.0, 6.0]

italo.sort(reverse=True)
medina.sort(reverse=True)
print(italo, medina)
if sum(italo[:2]) > sum(medina[:2]):
    print("Italo ganhou")
elif sum(italo[:2]) < sum(medina[:2]):
    print("Medina ganhou")
else: 
    print("Empate.")