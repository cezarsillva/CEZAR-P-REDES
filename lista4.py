# 10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
# que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
# jogadores, crie um programa que apresente as seguintes informações:

# • O peso médio e a idade média de cada um dos times;
# • O atleta mais pesado de cada time;
# • O atleta mais jovem de cada time;
# • O peso médio e a idade média de todos os participantes.
    

# somagerali = 0
# mediagerali= 0
# somageralp = 0
# mediageralp = 0
# pesomediotimes = 0
# idademediatimes = 0


# for paises in range (4):
#     for jogadores in range (2):
#         idade = int(input("Digite a idade do jogador: "))
#         peso = float(input("Digite o peso do jogador: "))


#         somagerali += idade
#         somageralp += peso
    

#     mediagerali = somagerali / 2
#     mediapeso = somageralp / 2

#     print(f'O peso médio e a idade média de cada um dos times é: ')------- ok
#     print(f'O atleta mais pesado de cada time é: ')
#     print(f'O atleta mais jovem de cada time é: ')

#     print(f' O peso médio de todos os participantes é: {mediapeso} e a idade média de todos os participantes: {mediagerali}')

# print(paises)

somatimesi = 0
mediatimesi= 0
somatimesp = 0
mediatimesp = 0

pesos = 0


print('\n')
for p in range (4):
    for j in range (3):
        idade = int(input("Digite a idade do jogador: "))
        peso = float(input("Digite o peso do jogador: "))
        #print(f'Time:{p}')
        print('\n')

        peso += peso
        somatimesi += idade
        somatimesp += peso
   

    mediatimesi = somatimesi / 3
    mediatimesp = somatimesp / 3



    print(f'====================================')
    print(f'O peso médio do time é: {mediatimesp} e a idade do time é: {mediatimesi}')
    print(f'====================================')
    print('\n')
