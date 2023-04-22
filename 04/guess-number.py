"""
Juego:

Por favor ingrese su nombre y elija un número del 1 al 100.
    a. Si el número está fuera del rango, se devolverá un mensaje indicando que ha salido del rango.
    b. Si el número es menor que el número aleatorio, se mostrará un mensaje de respuesta incorrecta y se indicará que el número a adivinar es menor.
    c. Si el número es mayor que el número aleatorio, se mostrará un mensaje de respuesta incorrecta y se indicará que el número a adivinar es mayor.
    d. Si adivina el número correctamente, habrá ganado y se mostrará cuántos intentos le tomó.
    e. Tenga en cuenta que dispone de 8 intentos para adivinar el número.

"""
import random

name = input('Ingresa tu nombre: ')
number_random = random.randint(1, 100)
tries = 8
print(f"""Bienvenido {name}
tienes 8 intentos para intentar adividar el número
el número tendrá un rango entre 1 y 100,
ten en cuanta, que si ingresas un número fuera del rango, perderás un intento !
""")
while tries > 0:
    print(f'Player: {name} - Intentos restantes: {tries}')
    number_picked = int(input('Ingrese un número del 1 al 100: '))
    tries -= 1
    if number_picked < 1 or number_picked > 100:
        print(
            f'El número {number_picked} tiene que ser en el rango de 1 y 100, has perdido 1 intento!')
    if number_picked > number_random:
        print(
            f'Respuesta incorrecta, el número secreto es menor a {number_picked}')
    if number_picked < number_random:
        print(
            f'Respuesta incorrecta, el número secreto es mayor a {number_picked}')
    if number_picked == number_random:
        print(
            f'Felicitaciones {name} !! Has ganado ! te sobraron: {tries} intentos')
        break
    if tries == 0:
        print(
            f'{name}, te has quedado sin intentos, el número secreto era: {number_random}')
