'''Archivo principal del juego Games'''
from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json


def main(archivo_torneo:str):
    '''Funcion principal del juego'''
    if archivo_torneo != "":
        with open(archivo_torneo, "r") as file:
            data = json.load(file)
    else:
        players_mexico = ['Chicharito', 'Piojo', 'Chucky', 'Tecatito', 'Gullit', 'Ochoa', 'Guardado', 'Herrera', 'Layun', 'Moreno', 'Araujo']
        players_españa = ['Casillas', 'Ramos', 'Pique', 'Alba', 'Iniesta', 'Silva', 'Isco', 'Busquets', 'Costa', 'Morata', 'Asensio']
        players_brasil = ['Neymar', 'Coutinho', 'Marcelo', 'Casemiro', 'Alisson', 'Thiago', 'Firmino', 'Jesus', 'Silva', 'Paulinho', 'Danilo']
        players_argentina = ['Messi', 'Aguero', 'Di Maria', 'Higuain', 'Mascherano', 'Otamendi', 'Rojo', 'Banega', 'Dybala', 'Perez', 'Mercado']
        lista_mexico = [Athlete(x) for x in players_mexico]
        lista_españa = [Athlete(x) for x in players_españa]
        lista_brasil = [Athlete(x) for x in players_brasil]
        lista_argentina = [Athlete(x) for x in players_argentina]
        soccer = Sport("Soccer", 11, "FIFA")
        mexico = Team("Mexico", soccer, lista_mexico)
        españa = Team("España", soccer, lista_españa)
        brasil = Team("Brasil", soccer, lista_brasil)
        argentina = Team("Argentina", soccer, lista_argentina)
        equipos = [mexico, españa, brasil, argentina]
        d = {}
        for local in equipos:
            for visitante in equipos:
                if local != visitante:
                    d[juego.to_json()['A']['name']] = juego.to_json()
        torneo = list(d.values())
        #juego = Game(mexico, españa)
        #torneo = [juego.to_json()]
        archivo_torneo = "torneo.json"
        with open(archivo_torneo, "w", encoding='utf-8') as f:
            json.dump(torneo, f, ensure_ascii=False, indent=4)
        print(f"Se escribió el archivo {archivo_torneo} con un torneo de {len(torneo)} juego(s)")
    #Jugar todos los juegos del torneo
    for juego in torneo:
        A = Team(juego['A']['name'], Sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'], Sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [Athlete(x['name']) for x in juego['B']['players']])
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")

if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)


