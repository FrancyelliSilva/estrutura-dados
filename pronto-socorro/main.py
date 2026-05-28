from fila import Fila

def menu():
    print("\n1 - Chegada")
    print("2 - Atender triagem")
    print("3 - Atendimento médico")
    print("4 - Sair")

    opcao = int(input("Digite a opção: "))

    return opcao

triagem = Fila()
verde = Fila()
vermelho = Fila()
medicos = Fila()

iniciar = ['Médico 1', 'Médico 2', 'Médico 3']
for i, medico in enumerate(iniciar):
    medicos.entrar(medico)

while True:
    opcao = menu()

    match opcao:
        case 1:
            nome = input("Nome paciente: ")
            triagem.entrar(nome)
            print(triagem.verFila())
        case 2:
            paciente = triagem.chamar()
            if paciente is not None:
                if len(paciente) >= 6:
                    print(f"Paciente {paciente} entrou na fila verde!")
                    verde.entrar(paciente)
                else:
                    print(f"Paciente {paciente} entrou na fila vermelha!")
                    vermelho.entrar(paciente)
            else:
                print(f"Não há pacientes na triagem!")
        case 3:
            medico = medicos.chamar()
            if medico is not None:
                if vermelho.isEmpty():
                    if not verde.isEmpty():
                        paciente = verde.chamar()
                        print(f"O {medico} chama o(a) {paciente} para atendimento.")
                        medicos.entrar(medico)
                        print(f"{medicos.verFila()}")
                    else:
                        print("Não há pacientes na fila")
                else:
                    paciente = vermelho.chamar()
                    print(f"O {medico} chama o(a) {paciente} para atendimento.")
                    medicos.entrar(medico)
                    print(f"{medicos.verFila()}")
            else:
                print(f"Não há médicos para atendimento")
        case 4:
            break
