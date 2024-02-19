'''
Exercícios sobre os comandos de condição em python
'''

#print(f'===========================================================================') 

#def q01():

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.



#valor1 = int(input ('Digite o primeiro valor: '))
#valor2 = int(input ('Digite o segundo valor: '))



#soma = valor1 + valor2

#if soma > 10:


#print(f'A soma dos dois números é maior que 10 sendo ele: {soma}')

#else:

#print(f'Seu BURRO digite os números para que a soma seja maior que 10!!!')




#print(f'===========================================================================') 


#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.



#valor1 = int(input ('Digite o primeiro valor: '))
#valor2 = int(input ('Digite o segundo valor: '))



#soma = valor1 + valor2

#if soma > 20:


    #print(f'A soma dos dois números é maior que 20 então soma - se com 8 sendo que o resultado é: {soma + 8}')

#else:

    #print(f'A soma dos dois números é menor ou igual a 20 então subtrae - se com 5 sendo que o resultado é: {soma - 5}')




#print(f'===========================================================================') 

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".



#valor = int(input ('Digite o valor: '))
#if valor % 3 == 0:
    #print(f'É múltiplo de 3.')
#else:
    #print(f'não é múltiplo de 3.')



#print(f'===========================================================================')

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.



#valor = int(input ('Digite o valor: '))


#if valor % 5 == 0:


    #print(f'É divisivel por 5.')
#else:
    #print(f'Não é divisivel por 5.')



#print(f'===========================================================================')


#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.



#valor = int(input ('Digite o valor: '))


#if valor % 3 == 0 and valor % 7 == 0 :


    #print(f'É divisivel por 3 e 7.')
 

#else:

    #print(f'Não é divisivel por 3 e 7.')



#print(f'===========================================================================')

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.


#salariobruto = float(input ('Digite o salário bruto: '))
#valorprestação = float(input ('Digite o valor da prestação: '))


#if valorprestação > salariobruto * 0.3:

    #print(f'Empréstimo não autorizado.')
 
#else:

    #print(f'Empréstimo autorizado.')


#print(f'===========================================================================')

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.




#num = int(input ('Digite o número: '))


#if 20 <= num <= 50:


    #print(f'Está entre o intevalo desejado.')


#else:

    #print(f'Não está  entre o intevalo desejado.')



#print(f'===========================================================================')

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".


#num = int(input ('Digite o número: '))


#if num > 20:


    #print(f'Maior do que 20.')



#if num == 20:

    #print(f'Igual a 20.')


#if num < 20:

    #print(f'Menor do que 20.')



#print(f'===========================================================================')

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.



#Ano_nasc = int(input ('Digite o ano de nascimento: '))
#Ano_atual = int(input ('Digite o ano atual: '))

#idade = 0

#if (Ano_nasc > Ano_atual):
    #print(f'Ano de nascimento inválido.')

#elif (Ano_nasc < Ano_atual):
    #idade = Ano_atual - Ano_nasc

#print(f'A idade é {idade} anos.')


#print(f'===========================================================================')

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.


#num1 = int(input ('Digite o primeiro número: '))
#num2 = int(input ('Digite o segundo número: '))
#num3 = int(input ('Digite o terceiro número: '))


#if num1 < num2 < num3:
    
    #print(f' {num1} - {num2} - {num3} ')

#elif num1 < num3 < num2:
    
    #print(f' {num1} - {num3} - {num2} ')

#elif num2 < num1 < num3:
    
    #print(f' {num2} - {num1} - {num3} ')

#elif num2 < num3 < num1:
    
    #print(f' {num2} - {num3} - {num1} ')

#elif num3 < num1 < num2:
    
    #print(f' {num3} - {num1} - {num2} ')

#elif num3 < num2 < num1:
    
    #print(f' {num3} - {num2} - {num1} ')


#print(f'===========================================================================')
#11. Faça um programa que leia 3 números e imprima o maior deles.



#num1 = int(input ('Digite o primeiro número: '))
#num2 = int(input ('Digite o segundo número: '))
#num3 = int(input ('Digite o terceiro número: '))

#if num1 > num2 > num3:
    
    #print(f' {num1}  ')

#elif num1 > num3 > num2:
    
    #print(f' {num1} ')

#elif num2 > num1 > num3:
    
    #print(f' {num2} ')

#elif num2 > num3 > num1:
    
    #print(f' {num2} ')

#elif num3 > num1 > num2:
    
    #print(f' {num3} ')

#elif num3 > num2 > num1:
    
    #print(f' {num3} ')



#print(f'===========================================================================')
#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos

#idade = int(input ('Digite sua idade. '))

#if idade > 18:
    #print(f' Você é maior de idade. ')

#elif idade < 18:
    #print(f' Você é menor de idade. ')

#elif idade >= 65:
    #print(f' Você já é considerado idoso ')



#print(f'===========================================================================')

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).

#nome = str(input ('Digite o nome do aluno: '))
#nota1 = float(input ('Digite a 1º nota do aulno: '))
#nota2 = float(input ('Digite a 2º nota do aluno: '))

#media = (nota1 + nota2 / 2)

#print(f' Aluno: {nome} ')
#print(f' Nota 1 do aluno: {nota1} ')
#print(f' Nota 2 do aluno: {nota2} ')
#print(f' A média do aulno é: {media} ')

#if media >= 7:
    #print(f' Aluno aprovado ')

#if media < 3:
    #print(f' Aluno reprovado ')

#else:
    #print(f'O Aluno  ficou de prova final ')

#print(f'===========================================================================')

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%


#salario = float(input ('Digite o salário bruto do funcionário: '))

#if salario <= 600:
    #print(f' Salário isento. ')

#elif salario > 600 and salario <= 1200:

    #print(f' Salário terá um desconto de 20% :{salario*20/100}. ')

#elif salario > 1200 and salario < 2000:

    #print(f' Salário terá um desconto de 25% :{salario*25/100} . ')

#elif salario >= 2000:

    #print(f' Salário terá um desconto de 30% :{salario*30/100} . ')



#print(f'===========================================================================')
 
#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.

#valorproduto = float(input ('Digite o valor do produto em R$: '))

#lucro1 = valorproduto * 45 / 100
#lucro2 = valorproduto * 30 / 100

#if valorproduto < 20:
    #print(f'O valor da venda é: {valorproduto + lucro1}')


#else:
    #print(f'O valor da venda é: {valorproduto + lucro2}')


#print(f'===========================================================================')

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos


#idade = int(input('Digite a idade do atleta: '))


#if idade >= 5 and idade <= 7:
    #print(f'A categoria do atleta é: Infantil A ')

#elif idade >= 8 and idade <= 10:
    #print(f'A categoria do atleta é: Infantil B ')


#elif idade >= 11 and idade <= 13:
    #print(f'A categoria do atleta é: Juvenil A ')

#elif idade >= 14 and idade <= 17:
    #print(f'A categoria do atleta é: Juvenil B ')

#elif idade >= 18:
    #print(f'A categoria do atleta é: Sênior ')


#print(f'===========================================================================')

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00


#nome = str(input('Digite o nome da pessoa: '))
#idade = int(input('Digite a idade da pessoa: '))


#if idade < 10:
    #print(f'O beneficiário {nome} tem  {idade} anos e deverá pagar R$30,00 de plano. ')


#elif idade >= 10 and idade <= 29:
    #print(f'O beneficiário {nome} tem  {idade} anos e deverá pagar R$60,00 de plano. ')


#elif idade >= 29 and idade <= 45:
    #print(f'O beneficiário {nome} tem  {idade} anos e deverá pagar R$120,00 de plano. ')


#elif idade >= 45 and idade <= 59:
    #print(f'O beneficiário {nome} tem  {idade} anos e deverá pagar R$150,00 de plano. ')


#elif idade >= 59 and idade <= 65:
    #print(f'O beneficiário {nome} tem  {idade} anos e deverá pagar $250,00 de plano. ')


#elif idade > 65:
    #print(f'O beneficiário {nome} tem  {idade} anos e deverá pagar R$400,00 de plano. ')


#print(f'===========================================================================')

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.


mês = int(input('Digite um valor entre 1 e 12: '))


if (mês == 1):

 print(mês, ' = Janeiro')

elif (mês == 2):

 print(mês, ' = Fevereiro')

elif (mês == 3):

 print(mês, ' = Março')

elif (mês == 4):

 print(mês, ' = Abril')

elif (mês == 5):

 print(mês, ' = Maio')

elif (mês == 6):

 print(mês, ' = Junho')

elif (mês == 7):

 print(mês, ' = Julho')

elif (mês == 8):

 print(mês, ' = Agosto')

elif (mês == 9):

 print(mês, ' = Setembro')

elif (mês == 10):

 print(mês, ' = Outubro')

elif (mês == 11):

 print(mês, ' = Novembro')

elif (mês == 12):

 print(mês, ' = Dezembro')

else:

 print('Digite um número no intervalo solicitado.')


#print(f'===========================================================================')

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

#print(f'===========================================================================')

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano 180cal Abacaxi 75cal   Chá 20cal
#Peixe 230cal   Sorvete diet 110cal Suco de laranja 70cal
#Frango 250cal  Mousse diet 170cal  Suco de melão 100cal
#Carne 350cal   Mousse chocolate 200cal Refrigerante diet 65cal

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos