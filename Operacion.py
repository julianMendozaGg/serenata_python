from random import randint, uniform, random
class Operacion():
    def __init__(self):
        self.numero=0
        super().__init__()
    
    def generarNumeroMusicos(self):
        self.numero= randint(5,10)
        return self.numero

    def escogerInstrumento(self):
        self.numero= randint(0,4)
        return self.numero