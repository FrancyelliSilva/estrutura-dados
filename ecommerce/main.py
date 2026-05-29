from pilha import Pilha

def menu():
    print("1 - Registrar Entrada em Centro de Distribuição")
    print("2 - Registrar Recusa / Retroceder um Passo")
    print("3 - Localização Atual da Carga")
    print("4 - Relatório de Rota de Ida Completa")
    print("5 - Sair")

    opcao = int(input("\nDigite a opção que deseja para prosseguir: "))
    return opcao

local = Pilha()
rota = Pilha()

while True:
    opcao = menu()

    if opcao == 1:
        endereco = input("Digite o local de entrada: ")
        local.push(endereco)
        rota.push(endereco)
        print(local.verEndereco())
    if opcao == 2:
        atual = local.pop()
        rota.push(atual)
        if atual is None:
            if not local.isEmpty():
                print(f"Logística Reversa ativada. Mercadoria saindo de: {atual}")
        else:
            print("Mercadoria já se encontra com o vendedor original")
    if opcao == 3:
        localiza = local.top()
        if not local.isEmpty():
            print(f"O pacote esta localizado em {localiza}")
        else:
            print("Mercadoria esta com o vendedor")
    if opcao == 4:
        print(f"{rota.rota()}")
    if opcao == 5:
        break



