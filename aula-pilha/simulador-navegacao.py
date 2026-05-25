def simulador_navegacao():
    historico = []
    avanco = []
    atual = None

    while True:
        comando = input().strip()

        if comando.startswith("visitar "):
            url = comando [8:].strip()
            if atual is not None:
                historico.append(atual)
            atual = url
            avanco.clear()
            print(f"Página visitada: {url}")

        elif comando == "voltar":
            if not historico:
                print("Não há página anterior.")
            else:
                avanco.append(atual)
                atual = historico.pop()
                print(f"Voltou para: {atual}")

        elif comando == "voltar":
            if not historico:
                print("Não há página anterior.")
            else:
                avanco.append(atual)
                atual = historico.pop()
                print(f"Voltou para: {atual}")
        
        elif comando == "avancar":
            if not avanco:
                print("Não há próxima página.")
            else: historico.append(atual)
            atual = avanco.pop()
            print(f"Avançou para: {atual}")

        elif comando == "mostrar":
            if atual is None:
                print("Nenhuma página visitada.")
            else:
                print(f"Página atual: {atual}")
        
        elif comando == "sair":
            break
    
simulador_navegacao()