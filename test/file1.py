#metodo no str
class  Pais:
    nombre = str
    idioma = str
    divisa = str
    km = float
    
    def __init__(self,nombre, idioma, divisa, km):
            self.nombre = nombre
            self.idioma = idioma
            self.divisa = divisa
            self.km = km
    
    
object3 = Pais("Ecuador","Español","Dolar", 24.0000)
print(object3)

#def __init__(self,nombre,idioma,divisa):
   # self.nombre = nombre
    #self.idioma =idioma
    #self.divisa = divisa
#object4 = Pais(

#print(Pais.divisa)
#print(Pais.nombre)
#print(Pais.idioma)
