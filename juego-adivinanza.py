

from importlib import import_module
from pickle import TRUE
import random


numero_secreto = random.randint(0,99)
cant_intentos= 0
cant_max_intentos = 5
adivinado = False

print("Bienvenidos al juego de adivinar numeros secreto!")

while not adivinado:
       
       if not cant_intentos < cant_max_intentos:
         print("Game over! Has superado la cantidad de 5 intentos")
         break

       entrada = input("Introduce el numero de 0 a 99: ")
       numero = int(entrada)


       if numero == numero_secreto:
        print("Has adivinado el numero secreto!")
        adivinado = TRUE

       elif numero < numero_secreto:
        print("El numero es mayor al ingresado")

       else:
        print("El numero es menor al ingresado")

        cant_intentos += 1  













    
    






