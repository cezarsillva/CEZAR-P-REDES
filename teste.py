total_consumo_residencial = 0
total_consumo_comercial = 0
total_consumo_industrial = 0

total_consumidores_tipo1 = 0
total_consumidores_tipo2 = 0

total_consumo_tipo1 = 0
total_consumo_tipo2 = 0

#preco_por_kwh = 0

print('\n')
for x in range(4):
    print(f'#####################################################################################################################')
    print(f'Consumidor:{x+1}')
    print('\n')

    erro=True
    while erro == True:
        try:
            numero_consumidor = int(input("Digite o número do consumidor: "))
            erro=False
        except ValueError:
            print(f'Valor Invalido, Digite apenas numeros inteiros.')
            erro=True
    erro=True
    while erro == True:
        try:
            quantidade_kwh = float(input("Digite a quantidade de kWh consumidos durante o mês: "))
            erro=False
        except ValueError:
            print(f'Valor Invalido, Digite o valor em números reais.')
            erro=True
    erro=True
    while erro == True:
        try:
            tipo_consumidor = int(input("Digite o tipo de consumidor (1 - residencial, 2 - comercial, 3 - industrial): "))
            if tipo_consumidor < 1 or tipo_consumidor > 3:
                raise ValueError('Valor inválido')
            erro=False
        except ValueError:
            print(f'Valor Invalido, Digite apenas o número 1 , 2 ou 3.')
            erro=True
        finally:
            print(f'Insira a informação do próximo consumidor!!!!!!')

    if tipo_consumidor == 1:
        preco_por_kwh = 0.3
        total_consumo_residencial += quantidade_kwh
        total_consumidores_tipo1 += 1
        total_consumo_tipo1 += quantidade_kwh
    elif tipo_consumidor == 2:
        preco_por_kwh = 0.5
        total_consumo_comercial += quantidade_kwh
        total_consumidores_tipo2 += 1
        total_consumo_tipo2 += quantidade_kwh
    elif tipo_consumidor == 3:
        preco_por_kwh = 0.7
        total_consumo_industrial += quantidade_kwh
    
    
    custo_total = quantidade_kwh * preco_por_kwh

    print('\n')
    print('----------------------------------------------------------------------------')
    print(f"O custo total para o consumidor {numero_consumidor} é: R$ {custo_total:.2f}")
    print('----------------------------------------------------------------------------')
media_consumo_tipo1 = total_consumo_tipo1 / total_consumidores_tipo1 if total_consumidores_tipo1 != 0 else 0
media_consumo_tipo2 = total_consumo_tipo2 / total_consumidores_tipo2 if total_consumidores_tipo2 != 0 else 0


print("Resumo:")

print(f"Total de consumo residencial: {total_consumo_residencial} kWh")
print(f"Total de consumo comercial: {total_consumo_comercial} kWh")
print(f"Total de consumo industrial: {total_consumo_industrial} kWh")
print(f"Média de consumo do tipo 1: {media_consumo_tipo1:.2f} kWh")
print(f"Média de consumo do tipo 2: {media_consumo_tipo2:.2f} kWh")
print('\n')
print(f'#####################################################################################################################')