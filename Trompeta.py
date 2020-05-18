from Instrumento import *
class Trompeta (Instrumento):
    def __init__(self):
        super().__init__()
        self.nombre="Trompeta"

    def prepararInstrumento(self):
        return "Afinando "+self.nombre
    
    def tocarInstrumento(self):
        return "Tocando "+self.nombre

