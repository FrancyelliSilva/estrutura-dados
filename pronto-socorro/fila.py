class Fila:
    def __init__(self):
        self._triagem = []      

    def entrar(self, pacientes):
        self._triagem.append(pacientes)
    
    def chamar(self):
        if len(self._triagem) > 0:
            return self._triagem.pop(0)
        return None
            
    def size(self):
        return len(self._triagem)
    
    def isEmpty(self):
        return len(self._triagem) == 0   

    def verFila(self):
        return list(self._triagem)

    def verMedicos(self):
        return list(self._medicos)

    def chamarMedico(self):
        return self._medicos.pop(0)

    def entrarMedico(self, medico):
        self._medicos.append(medico)
    

