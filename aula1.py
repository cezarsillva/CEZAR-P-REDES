print('funciona!!!!')
nota1 = 7
print(nota1)
print(type(nota1))

print(f'nota1 tem valor {nota1} e é tipo {type(nota1)} ')
nota2 = 7.3
print(f'nota1 tem valor {nota2} e é tipo {type(nota2)} ')
aluno = 'Maria'
print(f'aluno tem valor {aluno} e é tipo {type(aluno)} ')
media = (nota1 + nota2) / 2
print(f'{aluno}\n{nota1}\n{nota2}\n{media} ')

soma = nota1 + nota2
divisao = nota1 / nota2
multiplicacao = nota1 * nota2
subtracao = nota1 - nota2
resto_divisao = nota1 % nota2


#exemplo de interação do usuario.

#nome = input ('Digite seu nome:')
#print(f'Olá {nome}. Seja bem vindo(a)!')

# leia dois valores numericos e apresente o resto da divisão.


#nota1 = int(input ('Digite a primeira nota:'))
#nota2 = int(input ('Digite a segunda nota:'))

#resto = nota1 % nota2

#print(f'{nota1} % {nota2} = {resto}')


valor = float(input ('Digite o valor do produto:'))
desconto = float(input ('Digite o desconto do produto:')) 

valortotal = valor * (1 - desconto / 100)

print(f'O valor do produto é {valortotal}.')
