## Declaración de Clases

class Vehiculo:
   _color = ""
   _ruedas = 0
   _puertas = 0

   def getColor(self):
      return self._color
   
   def setColor(self,value):
      self._color = value

   def getRuedas(self):
      return self._ruedas
   
   def setRuedas(self,value):
      self._ruedas = value

   def getPuertas(self):
      return self._puertas
   
   def setPuertas(self,value):
      self._puertas = value

class Coche(Vehiculo):

   _velocidad = 0
   _cilindrada = 0

   def __init__(self):
      self.setPuertas(4)
      self.setRuedas(5)

   def getVelocidad(self):
      return self._velocidad
   
   def setVelocidad(self,value):
      self._velocidad = value

   def getCilindrada(self):
      return self._cilindrada
   
   def setCilindrada(self,value):
      self._cilindrada = value

## Main

c1 = Coche()
c1.setCilindrada(1200)
c1.setColor("Rojo")
c1.setVelocidad(60)
print("Tenemos el coche1 de ",c1.getCilindrada(),"cc, con ",c1.getPuertas(), "puertas")
print("de color ",c1.getColor(), ", con ", c1.getRuedas(),"ruedas y una velocidad de ",c1.getVelocidad(), "km/h.")