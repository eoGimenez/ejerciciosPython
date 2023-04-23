"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""


def check_cero(*xargs):
    prev = 1
    for num in xargs:
        if num == 0 and prev == 0:
            return True
        prev = num

    return False


print(check_cero(5, 6, 1, 0, 0, 9, 3, 5))
print(check_cero(6, 0, 5, 1, 0, 3, 0, 1))
