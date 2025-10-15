import requests


URL = "https://pokeapi.co/api/v2/pokemon"
base = requests.get(URL).json()

def buscador_pokemon(nom_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nom_pokemon}"
    respuesta = requests.get(url).json()
    especie = url.replace("pokemon", "pokemon-species")
    especie = requests.get(especie).json()

    print(f"Nombre: {respuesta['name']}")
    print(f"ID: {respuesta['id']}")
    print(f"Peso: {respuesta['weight']}")
    print(f"Altura: {respuesta['height']}")
    print(f"tipos:  {[t['type']['name'] for t in respuesta['types']]}")

    url_espécie = especie["evolution_chain"]["url"]
    evoluciones = requests.get(url_espécie).json()
    for evo in evoluciones["chain"]["evolves_to"]:
        print(evo["species"]["name"])

    games = [entry["version"]["name"] for entry in respuesta["game_indices"]]
    print(set(games))


if __name__ == "__main__":
    nom_pokemon = input("introduce el nombre o numero de un pokemon: ")
    buscador_pokemon(nom_pokemon)
    