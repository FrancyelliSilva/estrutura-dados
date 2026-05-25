def navegador():
    historico = []
    avanco = []
    atual = None

    print("Comandos: visitar <url> | voltar | avancar | sair\n")

    while True:
        comando = input(">>").strip()

        if comando.startswith("visitar "):
            url = comando[8:].strip()
            if atual is not None:
                historico.append(atual)
            atual = url
            avanco.clear()
            print(f"Página visitada: {url}")
        
        elif comando == "voltar":
            if not historico:
                print("Não há páginas para voltar.")
            else:
                avanco.append(atual)
                atual = historico.pop()
                print(f"Voltando para: {atual}")
        
        elif comando == "avancar":
            if not avanco:
                print("Não há páginas para avançar.")
            else:
                historico.append(atual)
                atual = avanco.pop()
                print(f"Avançando para: {atual}")

        elif comando == "mostrar":
            print(f"Página atual: {atual}" if atual else "Nenhuma página visitada.")

        elif comando == "sair":
            break

navegador()