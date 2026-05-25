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
print(verificar_demilitadores(expressao))
