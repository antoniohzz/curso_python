'''Lógica de la puntuacion del juego'''
from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game

def fifa(torneo:list):
    '''Grupo de la FIFA'''
    puntos = {'G:': 3, 'E:': 1, 'P:': 0}
    tablero = {}
    for juego in torneo:
        equipo_local = juego.get("A")
        equipo_visitante = juego.get("B")
        if equipo_local not in tablero:
            tablero[equipo_local] = {
                'G':0,
                'E':0,
                'P':0
            }
        if equipo_visitante not in tablero:
            tablero[equipo_local] = {
                'G':0,
                'E':0,
                'P':0
            }
    for juego in torneo:
        equipo_local = juego.get("A")
        equipo_visitante = juego.get("B")
        goles_local = juego.get("score")[0]
        goles_visitante = juego.get("score")[1]
        if goles_local > goles_visitante:
            tablero[equipo_local]['G'] += 1
            tablero[equipo_visitante]['P'] += 1
        elif goles_local < goles_visitante:
            tablero[equipo_local]['P'] += 1
            tablero[equipo_visitante]['G'] += 1
        else:
            tablero[equipo_local]['E'] += 1
            tablero[equipo_visitante]['E'] += 1