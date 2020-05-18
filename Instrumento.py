from abc import ABC, abstractmethod


class Instrumento (ABC):

    def __init__(self):
        pass

    @abstractmethod
    def prepararInstrumento(self):
        pass

    @abstractmethod
    def tocarInstrumento(self):
        pass




