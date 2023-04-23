"""
crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.

Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.

Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.

Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
"""


def devolver_distintos(num1, num2, num3):
    aux_list = [num1, num2, num3]
    total = sum(aux_list)
    if total > 15:
        return max(aux_list)
    if total < 10:
        return min(aux_list)
    if 10 <= total <= 15:
        aux_list.remove(max(aux_list))
        return max(aux_list)


print(devolver_distintos(3, 4, 5))
print(devolver_distintos(8, 4, 5))
print(devolver_distintos(1, 3, 5))
