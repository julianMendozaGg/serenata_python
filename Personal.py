from EquipoMaterial import *
from Operacion import *


class Personal():

    def __init__(self):
        self.azarInst = 0  # Este "azarInst" nos ayuda a escoger instrumentos al azar de listaEquipo

        # Este "numero" nos ayuda a saber la cantidad de musicos
        self.numero = Operacion().generarNumeroMusicos()
        self.listaEquipo = EquipoMaterial().alistarEquipo()
        self.equipoEscogido=[]
        super().__init__()

    def asignarInstrumentos(self):
        for i in range (self.numero):
            self.azarInst=Operacion().escogerInstrumento()
            self.equipoEscogido.insert(i,self.listaEquipo[self.azarInst])
        
        return self.equipoEscogido

    def compadreEmpiezeATocar(self):
        self.listaMetodo=self.asignarInstrumentos()
        for i in range(len(self.asignarInstrumentos())):
            print(self.listaMetodo[i].prepararInstrumento())
            print(self.listaMetodo[i].tocarInstrumento())
            
