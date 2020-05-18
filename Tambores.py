from Instrumento import *
# Tambores hereda de instrumento e iplementa sus metodos abstractos


class Tambores (Instrumento):

    def __init__(self):
        self.nombre = "Tambores"
        super().__init__()

    def prepararInstrumento(self):
        return "Probando " + self.nombre

    def tocarInstrumento(self):
        return "Tocando " + self.nombre
