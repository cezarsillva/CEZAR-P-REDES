maior = 0

for p in range (3):
    print(f'---------------------------------------')
    for j in range (2):

        print(f'time:{p+1}')
        print(f' jogador:{j+1}')

        peso = int(input("Digite o peso do jogador: "))

        if peso > maior:
            maior = peso

    print(f'O maior peso é {maior}Kg')








# maior = 0
# menor = 1000
# for c in range(1, 6):
#     n = int(input('Digite o peso da {} pessoa: '. format(c)))
#     if n > maior:
#         maior = n
#     if n < menor:
#         menor = n
# print('O menor peso é {}Kg e o maior peso é {}Kg'.format(menor, maior))