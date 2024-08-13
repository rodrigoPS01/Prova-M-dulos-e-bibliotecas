alunos = {}

def AdicionarAluno():
    matricula = int(input("Digite o número de matrícula do aluno: "))
    nome = str(input("Digite o nome do aluno: "))
    
    if matricula in alunos:
        print("Um aluno com essa matrícula já existe.")
    else:
        alunos[matricula] = nome
        print(f"Aluno {nome} adicionado com sucesso!")

def RemoverAluno():
    matricula = int(input("Digite o número de matrícula do aluno que deseja remover: "))
    
    if matricula in alunos:
        nome = alunos.pop(matricula)
        print(f"Aluno {nome} removido com sucesso!")
    else:
        print("Não foi encontrado nenhum aluno com essa matrícula.")

def AtualizarAluno():
    matricula = int(input("Digite o número de matrícula do aluno que deseja atualizar: "))
    
    if matricula in alunos:
        novo_nome = str(input(f"Digite o novo nome para o aluno {alunos[matricula]}: "))
        alunos[matricula] = novo_nome
        print(f"Nome do aluno atualizado para {novo_nome}!")
    else:
        print("Não foi encontrado nenhum aluno com essa matrícula.")

def VerAlunos():
    if alunos:
        print("Lista de alunos cadastrados:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
    else:
        print("Não há alunos cadastrados no momento.")


while True:
    menu = int(input('''
        1 - Adicionar aluno
        2 - Remover aluno
        3 - Atualizar aluno
        4 - Ver todos os alunos
        0 - sair
        '''))

    match menu:
        case 1:
            AdicionarAluno()
        case 2:
            RemoverAluno()
        case 3:
            AtualizarAluno()
        case 4:
            VerAlunos()
        case 0:
            break
        case _:
            print('Digite uma opção válida')
