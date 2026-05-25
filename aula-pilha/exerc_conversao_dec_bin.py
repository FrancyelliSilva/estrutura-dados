def decimal_para_binario(numero):
    if numero == 0:
        return "0"
    pilha = []
    while numero > 0:
        pilha.append(numero % 2)
        numero //= 2
    binario = ""
    while pilha:
        binario += str(pilha.pop())
    return binario

numero = int(input("Digite um número decimal: "))
print("Binário:", decimal_para_binario(numero))

