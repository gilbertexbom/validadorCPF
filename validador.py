# Validador do CPF
soma = 0
cont = 10
dv = 0


# Apresentação
print('\n\t\t\t -- Validador do CPF --')

cpf = input('Informe o cpf: ')

if(len(cpf) == 11):
    print(f'CPF {cpf} valido!')

    for i in range(0, 9):
        soma+=int(cpf[i])*cont
        cont-=1

    print(soma)

    resto = soma % 11

    print(resto)

    if resto >= 2:
        dv = 11 - resto
    else:
        dv = 0

    print(dv)

    if int(cpf[9]) == dv:
        print(f'Primeiro dígito {dv} válido!')
    else:
        print(f'Primeiro dígito {dv} INVÁLIDO!')

    cont = 11
    soma = 0

    for i in range(0, 10):
        soma+=int(cpf[i])*cont
        cont-=1

    print(soma)

    resto = soma % 11

    print(resto)

    if resto >= 2:
        dv = 11 - resto
    else:
        dv = 0

    print(dv)

    if int(cpf[10]) == dv:
        print(f'Segundo dígito {dv} válido!')
    else:
        print(f'Segundo dígito {dv} INVÁLIDO!')


else:
    print(f'CPF {cpf} INVÁLIDO!')

