"""
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
"""
import requests
URL = "https://pokeapi.co/api/v2/pokemon"
base = requests.get(URL).json()
#print(base)
"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
"""
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

buscador_pokemon("eevee")