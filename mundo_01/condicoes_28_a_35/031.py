#31. Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o
#preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para
#viagens mais longas.

distancia = float(input("Digite a distância da viagem em km: "))
preco = 0
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"O preço da viagem se {distancia}km será de R${preco:.2f}")
