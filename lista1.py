# https://github.com/ifmt-cba/lp20241

'''

###################################################################################

Exercícios sobre os comandos básicos em Python
'''

#print(f'------------------------------------------------------------------------') 

#1. Faça um programa que imprima o seu nome.

#print(f'exercicios 1') 


#nome = input ('Digite seu nome: ')
#print(f'Olá {nome}. Seja bem vindo(a)!')

#print(f'------------------------------------------------------------------------') 

#2. Faça um programa que imprima o produto dos valores 30 e 27.


#valor1 = int(input ('Digite o primeiro valor:'))
#valor2 = int(input ('Digite o segundo valor:'))

#produto = (valor1 * valor2)

#print(f'O valor do produto é : {produto}')


#print(f'------------------------------------------------------------------------') 


#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.


#valor1 = int(input ('Digite o primeiro valor:'))
#valor2 = int(input ('Digite o segundo valor:'))
#valor3 = int(input ('Digite o segundo valor:'))


#Média = ((valor1 + valor2 + valor3)/ 3)


#print(f'A média é : {Média}')

#print(f'------------------------------------------------------------------------') 

#4. Faça um programa que leia e imprima um número inteiro.


#numero= int(input ('Digite um numero inteiro:'))

#print(numero)

#print(f'------------------------------------------------------------------------') 

#5. Faça um programa que leia dois números reais e os imprima.


#numero1= int(input ('Digite o primeiro numero:'))
#numero2 = int(input ('Digite o segundo numero:'))


#print(f'O primeiro número é: {numero1} O segundo número é: {numero2}')

#print(f'------------------------------------------------------------------------') 

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.

#numero = int(input ('Digite o valor: '))


#print(f'{numero + 1}')
#print(f' {numero - 1}')

#print(f'------------------------------------------------------------------------') 

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.




#nome= str(input ('Digite o nome do cliente: '))
#endereço = str(input ('Digite o endereço do cliente : '))
#telefone = int(input ('Digite o telefone do cliente: '))

#print("\n")

#print(f'O nome do cliente é : {nome}\n')

#print(f'O endereço do cliente é : {endereço}\n')

#print(f'O telefone do cliente é : {telefone}\n')


#print(f'------------------------------------------------------------------------') 


#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.


#numero1= int(input ('Digite o primeiro numero:'))
#numero2 = int(input ('Digite o segundo numero:'))

#subtração = (numero1 - numero2)

#print(f'A subtração dos dois números são: {subtração}')


#print(f'------------------------------------------------------------------------') 

#9. Faça um programa que leia um número real e imprima ¼ deste número.

numero = float(input('Digite um número: '))

fração = numero * (1/4)

print(f'A quarta parte do numero {numero} é : {fração}')

#print(f'------------------------------------------------------------------------')
#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base + altura) e a área (base * altura).

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.