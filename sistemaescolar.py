# Lista que armazenará os alunos cadastrados
alunos = []

# Mantém o sistema funcionando até o usuário escolher sair
while True:

    # Exibe o menu principal
    print("\n=== SISTEMA ESCOLAR ===")
    print("1 - Cadastrar aluno")
    print("2 - Lançar notas")
    print("3 - Listar alunos")
    print("4 - Sair")

    # Recebe a opção do usuário
    opcao = input("Escolha: ")

    # Cadastro de aluno
    if opcao == "1":
        matricula = input("Matrícula: ")
        nome = input("Nome: ")

        # Salva os dados do aluno na lista
        alunos.append({
            "matricula": matricula,
            "nome": nome,
            "media": None
        })

        print("Aluno cadastrado com sucesso!")

    # Cadastro das notas e cálculo da média
    elif opcao == "2":
        matricula = input("Digite a matrícula do aluno: ")

        # Procura o aluno pela matrícula
        for aluno in alunos:
            if aluno["matricula"] == matricula:
                nota1 = float(input("Nota 1: "))
                nota2 = float(input("Nota 2: "))

                # Calcula a média
                aluno["media"] = (nota1 + nota2) / 2

                print("Média cadastrada com sucesso!")
                break
        else:
            print("Aluno não encontrado!")

    # Exibe os alunos cadastrados
    elif opcao == "3":
        for aluno in alunos:
            print(f"\nMatrícula: {aluno['matricula']}")
            print(f"Nome: {aluno['nome']}")

            # Verifica se a média existe e mostra a situação
            if aluno["media"] is not None:
                situacao = "Aprovado" if aluno["media"] >= 7 else "Reprovado"
                print(f"Média: {aluno['media']:.1f}")
                print(f"Situação: {situacao}")
            else:
                print("Média: Não cadastrada")

    # Encerra o sistema
    elif opcao == "4":
        print("Sistema encerrado!")
        break

    # Caso o usuário digite uma opção inválida
    else:
        print("Opção inválida!")