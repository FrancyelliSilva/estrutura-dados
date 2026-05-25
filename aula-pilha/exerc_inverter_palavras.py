def inverter_palavras(frase):
    resultado = []
    for palavra in frase.split():
        pilha = []
        for letra in palavra:
            pilha.append(letra)
        palavra_invertida = ""
        while pilha:
            palavra_invertida += pilha.pop()
        resultado.append(palavra_invertida)
    return " ".join(resultado)

frase = input("Digite uma frase: ")
print(inverter_palavras(frase))
