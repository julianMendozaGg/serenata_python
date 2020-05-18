from Instrumento import *


class Guitarra(Instrumento):

    def __init__(self):
        super().__init__()
        self.nombre = "Guitarra"

    def prepararInstrumento(self):
        return "Afinando "+self.nombre

    def tocarInstrumento(self):
        return "Tocando "+self.nombre



