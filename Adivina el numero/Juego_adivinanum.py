from random import *

lives = 8
intentos = 1
random_number = randint(1,100)
user_name = input("Hola, cual es tu nombre\n")
print(f"Mucho gusto, me llamo CPU, ahora bien {user_name}\nhe pensado un numero entre 1 y 100, tienes que adivinar\nel numero y solo tienes ocho intentos. ¡Buena suerte!")
while lives != 0:
    my_number = int(input("Digita tu numero\n"))
    if my_number not in range(1,101):
        print("Ha elegido un numero no permitido, vuelva a digitar otro")
        lives = lives - 1
        intentos = intentos + 1
    if my_number < random_number:
        print("El numero ingresado es menor al numero a encontrar")
        lives = lives - 1
        intentos = intentos + 1
    if my_number > random_number:
        print("El numero ingresado es mayor al numero a encontrar")
        lives = lives - 1
        intentos = intentos + 1
    if my_number == random_number:
        print(f"Felicidades, acertaste el numero, la cantidad de intentos fue {intentos}")
        break
if lives == 0:
    print(f"Se terminaron las vidas, el numero era {random_number} ¡GAME OVER!")