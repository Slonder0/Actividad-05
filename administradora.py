from particula import Particula

class Administradora:
    def __init__(self):
        self.__particulas = []
        
    def agregar_final(self,particula:Particula):
        self.__particulas.append(particula)
        
    def agregar_inicio(self,particula:Particula):
        self.__particulas.insert(0,particula)
        
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
            
            
part = Particula( origen_x= 10,origen_y= 20,destino_x= 13,destino_y=28)
part2 = Particula( origen_x= 5,origen_y= 23,destino_x= 13,destino_y=67)

admi = Administradora()

admi.agregar_inicio(part)
admi.agregar_final(part2)
admi.mostrar()

#admi.mostrar()
