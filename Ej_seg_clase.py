'''
1) Crear un modulo con cuatro funciones
    - Fecha, mostrar fecha de hoy , sys o os modulo
    - Potencia de un numero, math
    - Operar un File (R,W, R/W)
        - Crear un archivo (modo, nombre arch y contenido)
        - Leer un archivo (nombre archivo y contenido)

2)  Crear un File con formato JSON.
    Converti a diccionario desde ese archivo.
'''

from datetime import date
from math import pow

def read_file (_nombrefile, _modo="r"):
    f = open(_nombrefile, _modo)
    data = f.read()
    f.close()
    return data

def create_file (_nombrefile, _data, _modo="w"):
    f = open(_nombrefile, _modo)
    f.write(_data)
    f.close()


def getDate ():
    today = date.today()
    return today

def getpow(_val, _exp):
    return pow(int(_val), int(_exp))


def main():
    print (getDate())
    
    num = input("Ingrese un numero:")
    pot = input("Ingrese la potencia:")
    print("{} elevado a la potencia {} es {}".format(num, pot, getpow(num,pot)))
    
    texto = "texto de ejemplo"
    print(type(texto))
    create_file ("test.txt", str(texto))

    print read_file ("test.txt")

if __name__ == "__main__":
    main()

