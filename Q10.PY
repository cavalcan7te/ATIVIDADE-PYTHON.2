while True:
    print ('''
------------------------CALCULADORA.PYTHON------------------------
           0 - SAIR
           1 - SOMA
           2 - SUBTRAÇÃO
           3 - MULTIPLICAÇÃO
           4 - DIVISÃO
           5 - POTÊNCIA DE DOIS
------------------------------------------------------------------
            ''')
    n = int(input('Operação: '))
    if n == 1:
        print('SOMA')
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        print(f'{n1} + {n2} = {n1 + n2}')
    elif  n == 2:
        print('SUBTRAÇÃO')
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        print(f'{n1} - {n2} = {n1 - n2}')
    elif n == 3:
        print('MULTIPLICAÇÃO')
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        print(f'{n1} x {n2} = {n1 * n2}')
    elif n == 4:
        print('DIVISÃO')
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        print(f'{n1} : {n2} = {n1 / n2}')
    elif n == 5:
        print('POTÊNCIA DE DOIS')
        n1 = float(input('Digite um número: '))
        print(f'{n1}^2 = {n1 * n1}')
    else:
        if n == 0:
            break
        else:
            print('Número inválido, tente novamente.')
    continuar = int(input('''
                Deseja continuar?
                      SIM - 1
                      NÃO - 0
                      '''))
    if continuar == 0:
        break