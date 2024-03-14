
for x in range (4):
    
    quantidadekwh = float(input("Digite a quantidade de KWH /mês: "))
    codigotipoconsumidor = int(input('Informe o código do consumidor sendo: [1 = Residencial] [2 = Comercial] [3 = Industrial]: '))


    if codigotipoconsumidor == 1:
        print(F'O custo total do consumidor é: {quantidadekwh * 0.03}')

    if codigotipoconsumidor == 2:
        print(F'O custo total do consumidor é: {quantidadekwh * 0.05}')

    if codigotipoconsumidor == 3:
        print(F'O custo total do consumidor é: {quantidadekwh * 0.07}')

