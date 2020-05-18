from Instrumento import *


#Guitarra hereda de instrumento e iplementa sus metodos abstractos
class Guitarra(Instrumento):

    def __init__(self):
        super().__init__()
        self.nombre = "Guitarra"

    def prepararInstrumento(self):
        return "Afinando "+self.nombre

    def tocarInstrumento(self):
        return "Tocando "+self.nombre



