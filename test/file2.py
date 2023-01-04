from file1 import Pais
class Viaje:
    costo = float
    tiempo = float
    pais = Pais("","","","")
    
    def __init__(self,costo,tiempo,pais):
        self.costo = costo
        self.tiempo = tiempo
        self.pais = pais
        
#if __name__ == "__main__" :
    
object0 = Viaje(26.89,15.20,Pais("francia","frnaces","euro",1062.9))
print(object0)
    
 
    
  