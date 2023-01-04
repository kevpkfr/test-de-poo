#metodo str y herencia metodo hijos
class Habitad:
    
    ubicacion = str
    continente = str
    clima = str
    
    def __init__(self,  ubicacion, continente, clima):
        
        self.ubicacion = ubicacion
        self.continente = continente
        self.clima = clima
        
#CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO __str__
      
    def __str__(self):
        return f'Hola, yo habito en {self.ubicacion} {self.continente}, mi clima es  {self.clima}'
    
#REALIZAR UNA HERENCIA DENTRO DEL MISMO ARCHIVO DE UNA DE LAS CLASES CREADAS, CREANDO UN METODO STR EN EL HIJO (IMPRMIR UN OBJETO CON ESA CLASE) 
class Animal(Habitad):
    
    ciudad = str
    
    def __init__(self, ubicacion,continente,clima, ciudad): 
        super().__init__(ubicacion,continente,clima)   
        self.ciudad = ciudad
        
object3= Animal("belgica", "europa","helido","dussendolf")
#print(vars(Animal))
print(object3)   
    