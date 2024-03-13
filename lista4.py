#13. Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores
#de consumo. Para cada consumidor, são digitados os seguintes dados:

#• número do consumidor
#• quantidade de kWh consumidos durante o mês
#• tipo (código) do consumidor
#1-residencial, preço em reais por kWh = 0,3
#2-comercial, preço em reais por kWh = 0,5
#3-industrial, preço em reais por kWh = 0,7

#Os dados devem ser lidos até que seja encontrado o consumidor com número 0
#(zero). O programa deve calcular e imprimir:

#• O custo total para cada consumidor
#• O total de consumo para os três tipos de consumidor
#• Amédia de consumo dos tipos 1 e 2


#somacodigostipoconsumidor= 0
#somaquantidadekwh = 0

somakwhresidencial = 0
somakwhcomercial = 0
somakwhindustrial = 0

print('\n')
for x in range(6):
    print(f'====================================')
    print(f'Consumidor:{x+1}')
    print('\n')
    #numeroconsumidor = int(input("Digite o número do consumidor: "))
    quantidadekwh = int(input("Digite a quantidade de KWH /mês: "))
    #codigotipoconsumidor = int(input('Informe o código do consumidor sendo: [1=Residencial] [2=Comercial] [3=Industrial]: '))


    #somacodigostipoconsumidor += codigotipoconsumidor
    #somaquantidadekwh += quantidadekwh

totalkwhresidencial = somaresidencial += quantidadekwh
totalkwhcomercial = somacomercial += quantidadekwh
totalkwhindustrial = somaindustroal += quantidadekwh


#print('\n')
#print(f'Total de consumidor: {x}')
#print('\n')


    print('\n')
    if somacodigostipoconsumidor == 1:
        print(f'O custo total do consumidor residencial é: {totalkwhresidencial* 0.03}')

    print('\n')
    if somacodigostipoconsumidor == 2:
        print(f'O custo total do consumidor comercial é: {totalkwhcomercial * 0.05}')

    print('\n')
    if somacodigostipoconsumidor == 3:
        print(f'O custo total do consumidor industrial é: {totalkwhindustrial * 0.07}')







print('\n')





# print('\n')
# print(f'O total de consumo para todos os consumidores é: {somaquantidadekwh}')
# print('\n')



# print(f'O custo total do consumidor é: ')
# print(f'O total de consumo para todos os consumidores é:') ok
# print(f'A média de consumo para o tipo 1 é:')
# print(f'A média de consumo para o tipo 2 é:')





