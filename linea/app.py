'''
    Archivo principal de linea
'''

import funciones

def main(m,b):
    x = [x/10.5 for x in range(1,101,10)]
    y = [funciones.calcular_y(x,m,b) for x in x]
    print(x)
    print(y)
    coordenadas = list(zip(x,y))
    print(coordenadas)


if __name__ == "__main__":
    main(2,3)
