from fila import Fila

def menu():
    print("1 - Chegada ")
    print("2 - Atender triagem")
    print("3 - Atendimento médico")
    print("4 - Sair")
    opcao = int(input("Digite a opção: "))

    return opcao       

triagem = Fila()
verde = Fila()
vermelho = Fila()

while True:
    opcao = menu()

    match opcao:
        case 1:
            nome = input("Nome paciente: ")
            triagem.entrar(nome)
            triagem.verFila()
        case 2:
            paciente = triagem.chamar()
            if paciente != None:
                if len(paciente) > 6:
                    verde.entrar(paciente)
                    print(f"{paciente} entrou na fila verde")
                else:
                    vermelho(paciente)
                    print(f"{paciente} entrou na fila vermelha")
            else:
                print("Não há mais pacientes na fila de triagem")
        case 3:
            if vermelho.isEmpty():
                if not verde.isEmpty():
                    paciente = verde.chamar()
                    print(f"{paciente}")
                else:
                    print("Não há pacientes para atender")
            else:
                paciente = vermelho.chamar()
                print(f"{paciente}")
        case 4:
            break
        case 5:
            print("Opção Inválida")
