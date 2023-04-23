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
