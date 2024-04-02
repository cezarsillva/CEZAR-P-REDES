#20. Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:

#• Qual o seu time de coração?
#1-Fluminense;
#2-Botafogo;
#3-Vasco;
#4-Flamengo;
#5-Outros

#• Onde você mora?
#1-RJ;
#2-Niterói;
#3-Outros

#• Qual o seu salário?

#Faça um programa que imprima:
#• o número de torcedores por clube; --------------------------------------------------- ok
#• a média salarial dos torcedores do Botafogo;----------------------------------------- ok
#• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
#clubes;
#• o número de pessoas de Niterói torcedoras do Fluminense
#Obs.: O programa encerra quando se digita 0 para o time.


quantidadefluminense = 0
quantidadebotafogo = 0
quantidadevasco = 0
quantidadeflamengo = 0
quantidadeoutros = 0

quantidaderiodejaneiro = 0
quantidadeniteroi = 0
quantidadeoutrosenderecos = 0


totalbotafogo = 0.0

for x in range(3):
	print(f'-------------------------------------------------------------')
	print(f'Torcedor:{x+1}')
	print('\n')
	time = int(input('Digite o nome do time sendo Fluminense = 1 Botafogo = 2 Vasco = 3 Flamengo = 4 Outros = 5:  '))
	endereco = int(input('Digite o endereço do pesquisado sendo Rio de janeiro = 1 Niterói = 2 Outros = 3: '))
	salario = float(input('Digite o salario do pesquisado: '))

	if time == 1:
		quantidadefluminense += 1
		print(f' Torcedor do Fluminense.')
	elif time == 2:
        quantidadebotafogo += 1
        #totalbotafogo += salario
        print(f' Torcedor do Botafogo.')
	elif time == 3:        
		quantidadevasco += 1
		print(f' Torcedor do Vasco.')
	elif time == 4:        
		quantidadeflamengo += 1
		print(f' Torcedor do Flamengo.')
	elif time == 5:        
		quantidadeoutros += 1
		print(f' Torcedor de outros clubes.')
    else:
        print(f'O opção inválida.......')



	if endereco == 1:
		quantidaderiodejaneiro += 1
		print(f' Torcedor mora no Rio de janeiro.')
	elif endereco == 2:
		quantidadeniteroi += 1
		print(f' Torcedor mora em Niterói.')
	elif endereco == 3:        
		quantidadeoutrosenderecos += 1
		print(f' Torcedor mora em outras Cidades.')
    else:
        print(f'O opção inválida.......')

#mediabotafogo = totalbotafogo / quantidadebotafogo

print('\n')
print(f'----------------------------------------------------------------')

print(f'A média salarial dos torcedores do Botafogo é: {mediabotafogo} ')

print(f'----------------------------------------------------------------')

print('\n')

print(f'A quantidade de torcedores do Fluminense  é: {quantidadefluminense} ')

print(f'A quantidade de torcedores do Botafogo  é: {quantidadebotafogo} ')

print(f'A quantidade de torcedores do Vasco  é: {quantidadevasco} ')

print(f'A quantidade de torcedores do Flamengo  é: {quantidadeflamengo} ')

print(f'A quantidade de torcedores dos outros clubes  é: {quantidadeoutros} ')
