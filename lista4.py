#10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
#jogadores, crie um programa que apresente as seguintes informações:
#
#• O peso médio e a idade média de cada um dos times; ------ok
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.
    

somatimesi = 0
mediatimesi= 0
somatimesp = 0
mediatimesp = 0

somamediaidadet = 0
somamediapesot = 0

maior = 0
menor = 1000

print('\n')

for p in range (3):
    print(f'---------------------------------------')
    for j in range (2):

        print(f'time:{p+1}')
        print(f' jogador:{j+1}')

        idade = int(input("Digite a idade do jogador: "))
        peso = float(input("Digite o peso do jogador: "))
    
        if peso > maior:
            maior = peso

        if idade < menor:
            menor = idade

        print('\n')

        somatimesi += idade
        somatimesp += peso


    mediatimesi = somatimesi / 2
    mediatimesp = somatimesp / 2

    somamediaidadet += mediatimesi
    somamediapesot += mediatimesp

        


    print(f'====================================')

    print(f'O peso médio do time é: {mediatimesp}')
    print(f'A idade média do time é: {mediatimesi}')
    print(f'O atleta mais pesado do time tem: {maior} kg')
    print(f'O atleta mais jovem do time tem: {menor} anos.')
    
    print(f'====================================')
    
    
    somatimesi = 0
    mediatimesi= 0
    somatimesp = 0
    mediatimesp = 0

    maior = 0
    menor = 1000

    print('\n')

mediatodospi = somamediaidadet / 3
mediatodospp = somamediapesot / 3

print('\n')

print(f'O peso médio de todos os participantes é: {mediatodospp} e a idade média de todos os participantes é:{mediatodospi}')

print('\n')