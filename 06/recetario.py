"""
Aquí viene la consigna: tu código le va a dar primero la bienvenida al usuario, le va a informar 
la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar 
cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de 
estas opciones que tenemos aquí: 

1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que 
el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido. 
2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que 
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va 
a crear ese archivo en el lugar correcto. 
3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar 
una carpeta nueva con ese nombre. 
4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va 
a eliminar
5. La opción 5, le va a preguntar qué categoría quiere eliminar
6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código

"""


from io import open
from pathlib import Path

route_home = Path(
    "/Users/Eu/Documents/Eu/Visual-Studio/EjerciciosPython/06/recetas")


def welcome():
    counter = 0
    for txt in Path(route_home).glob("**/*.txt"):
        counter += 1

    print(f"""Bienvenido a su Recetario personal
La Ruta de la carpeta es:
{route_home}    
Actualmente cuentas con {counter} recetas""")


def select_category():
    return input("Seleccione una categoria: ").lower()


def read_recipe(category):
    que_es_esto = Path(route_home, category)
    recipies = []
    for index, txt in enumerate(que_es_esto.glob("*.txt")):
        recipies.append(txt.relative_to(que_es_esto))
        print(f"[{index+1}] - {txt.relative_to(que_es_esto)}")
    choice = int(input("Elija el número que corresponda a la receta a leer: "))
    to_read = Path(que_es_esto, recipies[choice-1]).read_text("utf-8")
    print(to_read)


def start_program():
    welcome()
    while True:
        print("""
        [1] - Leer una receta
        [2] - Crear una receta
        [3] - Crear una categoría
        [4] - Eliminar una receta
        [5] - Eliminar una categoría
        [6] - Salir del programa
        """)
        option = input("Elija una opción: ")
        if option == "6":
            break
        if option == "1":
            category_selected = select_category()
            read_recipe(category_selected)


start_program()
