#inversão de palavras

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
frase_invertida = inverter_palavras(frase)


#verificação de parenteses e demilitadores
def verificar_demilitadores(expressao):
    pilha = []
    pares = {')': '(', '}': '{', ']': '['}
    abertura = set('([{')
    
    for char in expressao:
        if char in abertura:
            pilha.append(char)
        elif char in ')}]':
            if not pilha or pilha[-1] != pares[char]:
                return "Expressão inválida"
            pilha.pop()
    
    return "Expressão válida" if not pilha else "Expressão inválida"
    
expressao = input("Digite uma expressão: ")
resultado = verificar_demilitadores(expressao)


#conversao decimal para binario
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


#desfazer