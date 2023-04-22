"""
Ingrese el primer dato, cualquiera.
Ingrese tres letras.

1-Analice cuántas veces se repite cada una de esas letras en la primera variable.
2-Cantidad de palabras.
3-¿Cuál es el primer y último carácter del texto?
4-Devolver la primera variable invertida, usar join.
5-Analizar si la palabra "python" aparece en el texto. ( Usando un Diccionario)
"""

primer_var = (input('Ingrese una frase, o palabra: ')).lower()
char_one = input('ingrese una letra: ').lower()
char_two = input('ingrese una letra: ').lower()
char_three = input('ingrese una letra: ').lower()
arr = list(char_one + char_two + char_three)
bool_diccionary = {True: 'se encuentra', False: 'no se encuentra'}


def repetidos(text: str, second):
    for char in second:
        print(f'La letra "{char}" se repite: {text.count(char)} veces!')


def palabras(text: str):
    return len(text.split())


def invertir(text):
    return (text[::-1])


def search(text):
    return 'python' in text


repetidos(primer_var, arr)
print(f'Tu texto tiene: {palabras(primer_var)} palabras')
print(
    f'De su texto, el primer caracter es: {primer_var[0]} y el ultimo es: {primer_var[-1]}')
print(f'EL texto invertido queda: {invertir(primer_var)}')
print(f'La palabra "Python" {bool_diccionary[search(primer_var)]}')
