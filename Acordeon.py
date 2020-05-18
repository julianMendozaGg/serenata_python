from Instrumento import *

#Acordeon hereda de instrumento e iplementa sus metodos abstractos
class Acordeon (Instrumento):

    def __init__(self):
        self.nombre="Acordeon"
        super().__init__()

    def prepararInstrumento(self):
        return "Afinando "+ self.nombre
    
    def tocarInstrumento(self):
        return "Tocando "+ self.nombre