'''
funciones auxilaries para el juego del ahorcado
'''

def carga_archivo_texto(archivo:str)->list:
    '''Carga un arcihivo de texto y devuelve una lista con las oraciones del archivo'''

    with open(archivo, 'r', encoding='utf-8') as f:
        oraciones = f.readlines()
    return oraciones

if __name__ == '__main__':
    lista = carga_archivo_texto('./ahorcado/plantillas/plantilla-0.txt')
    for elemento in lista:
        print(elemento)