"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.

Esta función va a mostrar en pantalla todos los números 
primos existentes en el rango que va desde cero hasta ese 
número incluido, y va a devolver la cantidad de números 
primos que encontró.

Aclaración, por convención el 0 y el 1 no se consideran primos.
"""


def is_prime(number):
    aux_prime = []
    for numb in range(2, number):
        is_divisible = False
        for num in range(2, numb):
            if numb % num == 0:
                is_divisible = True
                break
        if not is_divisible:
            aux_prime.append(numb)
    print(aux_prime)
    return len(aux_prime)


print(f"La cantidad de numeros primeros son: {is_prime(25)}")
