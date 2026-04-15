from flask import Flask, render_template, request
import requests  # Permite realizar las solicitudes HTTP a la API

appPokemon = Flask(__name__)  # nombre de la aplicacion "appPokemon"

def obtener_cadena_evolutiva(chain):
    """Recorre la cadena evolutiva y devuelve una lista de nombres en orden."""
    resultado = []
    actual = chain
    while actual:
        nombre = actual['species']['name']
        resultado.append(nombre)
        if actual['evolves_to']:
            actual = actual['evolves_to'][0]
        else:
            break
    return resultado

# Recordar que siempre que hay un @ se define la ruta de la aplicacion, y debajo se ejecuta el metodo.
@appPokemon.route('/', methods=['GET', 'POST'])
def index():
    pokemon = None  # Variable que almacena la información del pokemon
    if request.method == 'POST':
        # Obtiene el nombre del pokemon que ingresa el usuario.
        pokemonNombre = request.form.get('pokemon_name').lower()
        # Realiza la peticion a la PokeAPI
        busqueda = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemonNombre}')
        if busqueda.ok:  # Si encuentra al pokemon, obtiene la informacion y la almacena en un diccionario
            infoPokemon = busqueda.json()

            # Obtener la línea evolutiva
            speciesUrl = infoPokemon['species']['url']
            speciesData = requests.get(speciesUrl).json()
            evolutionUrl = speciesData['evolution_chain']['url']
            evolutionData = requests.get(evolutionUrl).json()
            cadenaEvo = obtener_cadena_evolutiva(evolutionData['chain'])

            # Obtener imagen de cada pokemon en la cadena evolutiva
            evolucionesInfo = []
            for evo in cadenaEvo:
                evoResp = requests.get(f'https://pokeapi.co/api/v2/pokemon/{evo}')
                if evoResp.ok:
                    evoData = evoResp.json()
                    evolucionesInfo.append({
                        'name': evo,
                        'image': evoData['sprites']['other']['official-artwork']['front_default']
                    })

            pokemon = {
                'name': infoPokemon['name'],
                'image': infoPokemon['sprites']['other']['official-artwork']['front_default'],
                'height': infoPokemon['height'],       # en decímetros
                'weight': infoPokemon['weight'],       # en hectogramos
                'types': [t['type']['name'] for t in infoPokemon['types']],
                'abilities': [h['ability']['name'] for h in infoPokemon['abilities']],
                'stats': [
                    {
                        'name': s['stat']['name'],
                        'value': s['base_stat'],
                        'percent': min(s['base_stat'], 150) / 150 * 100
                    }
                    for s in infoPokemon['stats']
                ],
                'base_experience': infoPokemon.get('base_experience', 'N/A'),
                'evoluciones': evolucionesInfo,
            }
        else:
            pokemon = 'no encontrado'
    return render_template('index.html', pokemon=pokemon)

if __name__ == '__main__':
    appPokemon.run(debug=True)
