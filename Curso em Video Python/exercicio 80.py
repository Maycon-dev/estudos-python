"""

Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre
-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista orde
nada na tela.

"""

lista = []

for c in range(0, 5):
    valor = int(input('Digite o valor:'))

    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1

print('=' * 50)
print(f'Os valores imprimidos foram {lista}')