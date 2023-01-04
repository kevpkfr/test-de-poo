#herencia simple 

class Alumno(object):  
    def __init__(self, edad, nombre,): 
        self.edad = edad 
        self.nombre = nombre
        
        
        
class DesarrolloDeSoftware (Alumno): 
                            
    def identificarse(self): 
        
       print (f"Soy {self.nombre} tengo {self.edad} años y estudio la carrera de desarrollo de software") 
       
Kevin = DesarrolloDeSoftware(24, 'Kevin pinsag') 
Kevin.identificarse() 