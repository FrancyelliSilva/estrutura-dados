def editor_texto():
    pilha_acoes = []
    texto_atual = ""

    print("Comandos:'voltar' para desfazer, 'sair' para encerrar")
    print("Qualquer outro texto segue normalmente.")


    while True:
        comando = input("Digite um comando ou texto: ").strip()

        if comando.lower() == "sair":
            print("Texto final:", texto_atual)
            print("Encerrando o editor de texto.")
            break
        elif comando.lower() == "voltar":
            if not pilha_acoes:
                print("Nada para desfazer.")
            else:
                acao_revertida = pilha_acoes.pop()
                texto_atual = pilha_acoes[-1] if pilha_acoes else ""
                print(f"Ação revertida: '{acao_revertida}' | Texto atual: '{texto_atual}'")
        else:
            texto_atual += comando
            pilha_acoes.append(texto_atual)
            print(f"Texto atual: '{texto_atual}'")

editor_texto()