'''
INF01040 - INTRODUÇÃO À PROGRAMAÇÃO
TURMA G
ALUNO: JOÃO GUILHERME DE SOUZA BARBOZA  
MATRÍCULA: 304260   
'''

operacao = 'x'
dict1 = dict()


print("~~~~ DIÁRIO DE CLASSE ~~~~")
while operacao != 'f':
    print('')
    print("Selecione uma operacao:")
    print("[a] - Inserir aluno")
    print("[m] - Calcular médias")
    print("[l] - Listar notas")
    print("[x] - Estatísticas")
    print("[f] - Finalizar programa")
    operacao = input("Informe uma operação: ")

    
    
    if operacao == 'a':
        # inserir um aluno na turma
        nome = input('Nome do aluno: ')
        n1 = float(input('Média dos LABs: '))
        n2 =  float(input('Média dos EPs: '))
        n3 = float(input('Média dos QTs: '))
        n4 = float(input('Nota da Prova 1: '))
        n5 = float(input('Nota da Prova 2: '))
        print(f'Aluno {nome} cadastrado com sucesso!\n')
        dict1[nome] = [n1,n2,n3,n4,n5]

    elif operacao == 'm':
        # calcular medias
        for aluno,n in dict1.items():
            AP = (0.4*n[0])+(0.4*n[1])+(0.2*n[2])
            n.append(AP)
            MP = (0.4*n[3]) + (0.6*n[4])
            n.append(MP)
            MEDIA = (AP + MP)/2
            n.append(MEDIA)
            print(f'ALUNO: {aluno}')
            print(f'NOTA PRATICA: {AP:.1f}')
            print(f'NOTA PROVAS: {MP:.1f}')
            print(f'== MEDIA: {MEDIA:.1f} ==')       
            print('')

    elif operacao == 'l':
        # listar notas
        print('[t] Mostrar todos os alunos')
        print('[r] Mostrar os alunos em recuperação')
        escolha = input('Escolha uma opção:')
        if escolha == 't':
            print('ALUNO\t\tMEDIA')
            for aluno,notas in dict1.items():
                print(f'{aluno.split()[0]}\t\t{notas[7]:.1f}')
        elif escolha == 'r':
            print('ALUNO\t\tMEDIA')
            for aluno,notas in dict1.items():
                if notas[7] < 6:
                    print(f'{aluno.split()[0]}\t\t{notas[7]:.1f}')
            
        
    elif operacao == 'x':
        # estatísticas da turma
        media = 0
        aprov = 0
        rec = 0
        for notas in dict1.values():
            media = media + notas[7]
            if notas[7] < 6:
                rec = rec + 1
            else:
                aprov = aprov + 1
                
        media = media/len(dict1)
        
        print('––––––––––––––––––––––')
        print(f'MEDIA DA TURMA: {media:.1f}')
        print(f'APROVADOS: {aprov} alunos')
        print(f'RECUPERAÇÃO: {rec} alunos')
        print('––––––––––––––––––––––')       
        

    elif operacao == 'f':
        # finalizar (não altere esta opção!)
        print('Saindo do Programa')
        break

    else:
        print("### Operação inválida. Tente novamente!")
    
