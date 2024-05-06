n1 = float(input('\033[34mDigite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n3:
    print('\033[32mOs segmentos podem formar um triangulo!!!', end=' ')
    if n1 == n2 == n3:
        print('\033[31mEQUILATERO!!!')
    elif n1 != n2 != n3 != n1:
        print('\033[31mESCALENO!!!')
    else:
        print('\033[31mISOCELES!!!')
else:
    print('\033[36mOs segmentos não podem formar um triangulo!!!')
