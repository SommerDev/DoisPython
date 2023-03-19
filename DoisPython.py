listaNumero = [] 
for i in range(0, 5):
    listaNumero.append(int(input(f'Digite um valor na posição {i}: ')))
    if i == 0:
        maior = menor = listaNumero[i]
    else:
        if listaNumero[i] > maior:
            maior = listaNumero[i]
        if listaNumero[i] < menor:
            menor = listaNumero[i]
print('=-' * 30)
print(f'Valores digitados na lista {listaNumero}')
print(f'O maior valor da lista é {maior}')
print(f'O menor valor da lista é {menor}')