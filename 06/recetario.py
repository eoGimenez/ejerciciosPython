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

import os
from io import open
from pathlib import Path


def clear():
    os.system('clear')


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
    categories = []
    print('La nueva lista de categorias:')
    for index, category in enumerate(route_home.glob("*")):
        categories.append(category.relative_to(route_home))
        print(f"[{index+1}] - {category.relative_to(route_home)}")
    choice = int(input("Seleccione el numero de la categoria: "))
    return categories[choice-1]


def read_recipe(category):
    category_route = Path(route_home, category)
    recipies = []
    for index, txt in enumerate(category_route.glob("*.txt")):
        recipies.append(txt.relative_to(category_route))
        print(f"[{index+1}] - {txt.relative_to(category_route)}")
    choice = int(input("Elija el número que corresponda a la receta a leer: "))
    to_read = Path(category_route, recipies[choice-1]).read_text("utf-8")
    clear()
    print(to_read)
    input('Cuando termine de leer su receta, presione ENTER')
    clear()


def write_recipe(category):
    category_route = Path(route_home, category)
    title_recipe = input('Ingrese el Titulo de la receta: ')
    body_recipe = ""
    while True:
        clear()
        print(f'Receta: {title_recipe}\n para aggregar un salto de linea precione "ENTER"\n Para terminar de excribir la receta\n escriba "salir" y se guardará automaticamente\n')
        new_line = input("|").lower()
        if new_line == "salir":
            clear()
            Path(
                f"{category_route}/{title_recipe}.txt").write_text(body_recipe, "utf-8")
            print(f'La receta: "{title_recipe}" ha sido creada correctamente!')
            break
        body_recipe += f"\n{new_line}"


def create_category():
    clear()
    new_category_name = input("Ingrese el nombre de la nueva Categoria: ")
    Path(route_home, new_category_name).mkdir()
    print('La nueva lista de categorias:')
    for category in route_home.glob("*"):
        print(f"{category.relative_to(route_home)}")


def delete_recipe(category):
    category_route = Path(route_home, category)
    recipies = []
    while True:
        clear()
        for index, txt in enumerate(category_route.glob("*.txt")):
            recipies.append(txt.relative_to(category_route))
            print(f"[{index+1}] - {txt.relative_to(category_route)}")
        choice = int(
            input("Elija el número que corresponda a la receta a ELIMINAR: "))
        to_delete = Path(category_route, recipies[choice-1]).read_text("utf-8")
        to_detete_path = Path(category_route, recipies[choice-1])
        clear()
        print(to_delete)
        delete_statement = input(
            'Esta es la receta que deceas eliminar ?? (Y/N)').lower()
        if delete_statement == "y":
            Path(to_detete_path).unlink()
            break


def delete_category(category):
    clear()
    category_route = Path(route_home, category)
    print("""
    ***************************************
    ************ ADVERTENCIA **************
    **                                   **
    ** Al borrar una categoria, eliminara**
    **   TODAS las recetas que contenga  **
    ** y no podrá RECUPERAR esas recetas **
    ***************************************

    """)
    delete_statement = input(
        f'Está a punto de eliminar la categoria\n"{category}", esta seguro ? (Y/N)').lower()
    if delete_statement == "y":
        for recipe in category_route.glob("*.txt"):
            Path(recipe).unlink()
        Path(category_route).rmdir()


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
        clear()
        if option == "6":
            clear()
            break
        if option == "1":
            category_selected = select_category()
            read_recipe(category_selected)
        if option == "2":
            category_selected = select_category()
            write_recipe(category_selected)
        if option == "3":
            create_category()
        if option == "4":
            category_selected = select_category()
            delete_recipe(category_selected)
        if option == "5":
            category_selected = select_category()
            delete_category(category_selected)


start_program()
