"""Ejercicio día 02"""

try:
    name = input("Cual es tu nombre: ")
    sales = int(input("Cuanto vendiste este mes ?: "))

    def bonus(to_calc):
        return round(to_calc * 0.13, 2)

    print(f"{name}: Has ganado {bonus(sales)} en Bonus!")
except ValueError as e:
    print("Ingrese un valor que corresponda!")
