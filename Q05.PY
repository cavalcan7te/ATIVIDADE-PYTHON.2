nome = input('Digite o nome do aluno: ')
disciplina = input('Digite o nome da disciplina: ')
nota = float(input('Digite a nota do aluno: '))

if nota < 0 or nota > 10:
    print('Nota inválida')
else:
    if nota >= 5.5 and nota < 6:
        nota = 6.0
   
        if nota < 6.0:
            status = ('reprovado')
        else:
            status = ('aprovado')
        print(f'{nome} está {status} em {disciplina} com nota {nota}')