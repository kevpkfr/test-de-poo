#REALIZAR UNA HERENCIA ENTRE ARCHIVOS CREANDO UN METODO EN EL HIJO
from file5 import Alumno
from file1 import Pais

class Universidad(Alumno):
    edad = int
    nombre = str
    pais = Pais("","","","")
    
    def __init__(self, nombre,edad,pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        
   
if __name__ == "__main__" : 
    
    objeto1 = Alumno(25 ,"Kevin Pinsag")
    print (vars(objeto1))
    objeto2 = Pais("Ecuador","Español","Dolar", 24.0000)
    print (vars(objeto2))
    
    #object4 = Alumno("kevin","Pinsag",24)
    objetox = Universidad("san francisco" , 20, Pais("Ecuador","Español","Dolar", 24.0000))
    
    #
    