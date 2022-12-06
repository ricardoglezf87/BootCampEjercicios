## Declaración de funciones

def esBisiesto(año):
   if(año%4 == 0):
      return True
   else:
      return False

## Main

año = eval(input("Intruduzca el año a comprobar: "))

if esBisiesto(año):
   print('El año introducido es bisiesto')
else:
   print('El año introducido no es bisiesto')