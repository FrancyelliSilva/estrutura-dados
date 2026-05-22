class Fila:

    def __init__ (self):
        self._pacientes = []

    def entrar(self, pacientes):
        self._pacientes.append(pacientes)

    def chamar(self):
        if len(self._pacientes) > 0:
            return self._pacientes.pop(0)
        return  None
    
    def size(self):
        return len(self._pacientes)
    
    def isEmpty(self):
        return len(self._pacientes) == 0

    def proximo(self):
        if not self.isEmpty():
            return self._pacientes[0]
        return None

    def verFila(self):
        print(self._pacientes)