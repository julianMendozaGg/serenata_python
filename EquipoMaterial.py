from Acordeon import *
from Guacharaca import *
from Guitarra import *
from Tambores import *
from Trompeta import *
class EquipoMaterial():

    def __init__(self):
        self.tambor=Tambores()
        self.guacharaca = Guacharaca()
        self.guitarra = Guitarra()
        self.trompeta = Trompeta()
        self.acordeon = Acordeon()
        super().__init__()

    def alistarEquipo(self):
        equipoInst=[self.acordeon,self.guacharaca,self.guitarra,self.tambor,self.trompeta]
        return equipoInst