## Declaración de Clases

class Alumno:
   _nombre = ""
   _notas = 0

   def getNombre(self):
      return self._nombre
   
   def setNombre(self,value):
      self._nombre = value

   def getNotas(self):
      return self._notas
   
   def setNotas(self,value):
      self._notas = value

## Main

c1 = Alumno()
c1.setNombre("Ricardo")
c1.setNotas(9.5)

print("Alumno:",c1.getNombre()," tiene una nota de: ",c1.getNotas())