class Pilha:
    def __init__(self):
        self._local = []

    def push(self, endereco):
        self._local.append(endereco)

    def verEndereco(self):
        return self._local

    def pop(self):
        return self._local.pop()

    def isEmpty(self):
        return len(self._local) == 0

    def top(self):
        return self._local[-1]

    def rota(self):
        return list(self._local)


    