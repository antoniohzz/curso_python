'''
funciones auxilaries para el juego del ahorcado
'''

def carga_archivo_texto(archivo:str)->list:
    '''Carga un arcihivo de texto y devuelve una lista con las oraciones del archivo'''

    with open(archivo, 'r', encoding='utf-8') as f:
        oraciones = f.readlines()
    return oraciones


def carga_plantillas(nombre_plantilla:str) -> dict:
    '''
    Carga las plantillas del juego a partir de un archivode texto
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./ahorcado/plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una plantilla del juego
    '''

    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)

def obten_palabras(lista:str)->list:
    '''
    Obtiene las palabras de un texto
    '''
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    return list(set_palabras)

if __name__ == '__main__':
    plantillas = carga_plantillas('plantilla')
    despliega_plantilla(plantillas, 5)
    lista_oraciones = carga_archivo_texto('./ahorcado/datos/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(lista_palabras[:50])


    