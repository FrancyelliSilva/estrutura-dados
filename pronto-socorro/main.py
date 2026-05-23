from fila import Fila

def menu():
    print("1 - Chegada")
    print("2 - Atender triagem")
    print("3 - Atendimento médico")
    print("4 - Sair")

    opcao = int(input("Digite a opção: "))

    return opcao

triagem = Fila()
verde = Fila()
vermelha = Fila()

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
                    vermelho.entrar(paciente)
                    print(f"{paciente} entrou na filha vermelha")
        case 3:
            if vermelho.isEmpty():
                if not verde.isEmpty():
                    
                    paciente = verde.chamar()