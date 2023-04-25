"""
Vas a crear el tunero para una farmacia que tiene tres áreas de atención: 
perfumería, farmacia, y cosméticos. Tu programa le tiene que preguntar al cliente a cuál de las áreas desea dirigirse, y le va a dar un número de 
turno según a qué área se dirija. Por ejemplo, si elige cosmética le va a dar el número C-54 
(“C” de cosmética). 
Luego de eso, nos va a preguntar si queremos sacar otro turno. Esto, en 
realidad, es para simular si viene un nuevo cliente. Y repetirá todo el proceso. 

Algunas cosas a tener en cuenta: 
Los diferentes clientes van a ir sacando turnos para diferentes áreas (perfumería, farmacia, 
cosmética), en diferentes órdenes, por lo que el sistema debe llevar la cuenta de cuántos turnos 
ha dado para cada una de esas áreas, y producir el siguiente número de cada área a medida 
que se lo pida.

"""
import os
from modulos import generator


def clear():
    return os.system('clear')


def turn_on():
    while True:
        print("""
             Saque su Turno

            [1] - Perfumería
            [2] - Farmacia
            [3] - Cosmética
            """)
        try:
            option = input("Ingrese el número para el area deseada: ")
            ["1", "2", "3"].index(option)
            if option == "1":
                ticket = generator.decoration(generator.perfumeria)
                ticket()
            if option == "2":
                ticket = generator.decoration(generator.farmacia)
                ticket()
            if option == "3":
                ticket = generator.decoration(generator.cosmetica)
                ticket()
        except Exception as e:
            clear()
            print("Por favor ingrese una opción valida !", e)
            input("Precione ENTER para volver al menu inicio")


turn_on()
