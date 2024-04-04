
PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para:       preti.joao@ifmt.edu.br
Assunto:    Prova 1 de Laboratório de Programação 2024/1
Mensagem:   CEZAR DA SILVA SOUZA
Anexo:      p1.py


Faça um programa que leia o valor unitário de um produto,

a quantidade desejada e imprima o valor total a pagar. (2,5pt)



print('--------------------------------------------------------')

somavalorproduto = 0

for x in range(2):
    print('\n')
    nomeproduto = str(input('Digite o nome do produto: '))
    valorproduto = float(input('Digite o valor do produto: '))


valorproduto += valorproduto

print(f'A quantidade de produtos é: {somavalorproduto}')



Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
  da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
  a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
  "Reprovado" ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
  reprovação e as demais em prova final). (2,5pt)

print('--------------------------------------------------------')
for x in range(2):
    print('\n')
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))


    media = (nota1 + nota2) / 2
    print('\n')
    print('--------------------------------------------------------')
    if media >= 7:
        print(f'Aluno {nome} provado a média é {media}')
    elif media > 3 and media < 7:
        print(f'Aluno em recuperação sua média é: {media}')
    elif media < 3:
        print(f'Aluno Reprovado')

    print('--------------------------------------------------------')
    print('\n')


3. Faça um programa que apresente um menu com 4 opções:
  [1] - Cadastrar
  [2] - Excluir
  [3] - Pesquisar
  [0] - Sair
  O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
  ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
  escolhida for zero (0). (2,5pt)


print('--------------------------------------------------------')

print('\n')

while True:
    opcao = int(input('Digite a opção de acordo com o desejado: Cadastrar = 1 Excluir = 2 Pesquisar = 3 Sair = 0: '))
    

    if opcao == 1:
        print('Seja bem vindo a Opção Cadastrar!!! ')
        break
        
    elif opcao == 2:
        print('Seja bem vindo a opção Excluir!!! ')
        break
    elif opcao == 3:
        print('Seja bem vindo a opção Pesquisar!!! ')
        break
    elif opcao == 0:
        print('Programa encerrado. ')
        break
    else:
        print('Opçâo inválida! Digite o número ao menu correspondente!!!')
        break




4. Faça um programa que calcule o retorno de um investimento. (2,5pt)
  O programa deve solicitar do usuário o:
  - valor que será investido;
  - prazo do investimento (meses);
  - juros mensal (juros composto).


valor = float(input('Digite o valor investido: '))
meses = float(input('Digite a quantidade de meses: '))
taxa = float(input('Digite o valor da taxa: '))



juro = (valor * taxa) / 100

total = (juro + valor) * 3

print(f'O investimento é: {total}')
