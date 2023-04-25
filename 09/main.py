# from pathlib import Path
# from zipfile import ZipFile

# with ZipFile("09/Proyecto+Dia+9.zip") as ziparch:
#     ziparch.extractall("09/")
import os
import math
from datetime import date
from pathlib import Path
import re
import time


def clear():
    return os.system("clear")


today = date.today()

ruta = Path(
    "/Users/Eu/Documents/Eu/Visual-Studio/EjerciciosPython/09/Mi_Gran_Directorio")


def serial_number_search(ruta):
    dictionary = {}
    for dirs, subdirs, files in os.walk(ruta):
        for file in files:
            search = Path(dirs, file)
            text = search.read_text("utf-8")
            serial_number = re.search(r"N\D{3}-\d{5}", text)
            if serial_number:
                dictionary[f"{file}"] = f"{serial_number.group()}"
            else:
                pass
    return dictionary


start = time.time()
dictionary_result = serial_number_search(ruta)
end = time.time()
result = end - start

clear()
print("-"*40)
print(f"Fecha de busqueda:\t{today.strftime('%d/%m/%Y')}\n")
print("ARCHIVOS\t\tNRO.SERIE")
print("-----------\t\t----------")
for key, value in dictionary_result.items():
    print(f'{key}\t\t{value}')
print(f'Numero encontrados: {len(dictionary_result)}')
print(f'Duración de la búsqueda: {math.ceil(result)}')
