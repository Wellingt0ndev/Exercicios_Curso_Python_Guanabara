#80 - Crie um programa onde o usuário possa digitar cinco valores numéricos e
#cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()).
#No final, mostre a lista ordenada na tela.

valores = list()
for c in range(0, 5):
    valor = int(input(f"Digite o valor: "))
    if c == 0 or valor > valores[-1]:
        valores.append(valor)
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                break
            pos += 1
print("=" * 40)
print(f"Os valores digitados em ordem foram {valores}")
