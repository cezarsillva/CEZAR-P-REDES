#18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
#serviços diários de:
#• R$15,00, se o número de dias for menor que 10;
#• R$8,00, se o número de dias for maior ou igual a 10;
#Faça umprograma que imprima o nome, a conta e o número da conta de cada
#cliente e ao final o total faturado pela pousada.
#O programa deverá ler novos clientes até que o usuário digite 0 (zero) como
#número da conta.

diasmenor10 = 15
diasmaior10 = 8
precodiaria = 30


print('\n')
for x in range(2):
    print(f'#####################################################################################################################')
    print(f'Cliente: {x+1}')
    print('\n')
    numeroconta = int(input('"Digite o número da conta: '))
    nomecliente = str(input('Digite o nome do cliente: '))
    numerodias = int(input('Digite a quantidade de dias na pousada: '))

    taxaservico1 = numerodias * 15
    taxaservico2 = numerodias * 8

    totalclientemenorque10 = precodiaria * numerodias + taxaservico1
    totalclientemaiorigual10 = precodiaria * numerodias + taxaservico2


    print('\n')
    
    if numerodias < 10:
        totalclientemenorque10 += 1
        print(f'O valor total pago pelo cliente {nomecliente} é: {totalclientemenorque10}')
    print('\n')
    if numerodias >= 10:
        totalclientemaiorigual10 += 1
        print(f'O valor total pago pelo cliente {nomecliente} é: {totalclientemaiorigual10}')
    print('\n')


    print(f'O faturamento total da pousada é: {totalclientemenorque10 + totalclientemaiorigual10} ')
