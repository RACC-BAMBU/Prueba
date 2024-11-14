
import requests

def buscarPokemon(nombrePokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombrePokemon.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon = response.json()
        print("Información del Pokémon:")
        print("-------------------------")
        print("Nombre:", pokemon['name'])
        print("-------------------------")
        print("ID:", pokemon['id'])
        print("-------------------------")
        print("Altura:", pokemon['height'])
        print("-------------------------")
        print("Peso:", pokemon['weight'])
        print("-------------------------")
        print("Tipos:")
        for tipo in pokemon['types']:
            print(" - ", tipo ['type']['name'])
            print("-------------------------")
    else:
        print("El Pokémon no existe en la PokeAPI")
    
    print("Estadísticas Base del Pokemon:")
    for stat in pokemon['stats']:
            print(f" - {stat['stat']['name'].capitalize()}: {stat['base_stat']}")

def main():
    while True:
        opcion = input("Ingrese el nombre de un Pokémon o escriba 'salir' para cerrar la Pokédex: ")
        if opcion.lower() == "salir":
            print("|_Pokedex apagada_|")
            break
        else:
            buscarPokemon(opcion)

if __name__ == "__main__":
    main()
    
    


"""
#1 - se escribe primero "import requests" ya que el requests permite hacer solisitudes de HTTP
en Python, y con la finalidad de hacer la solisitud GET al pokeapi 
y obtener información sobre el pokemon que vas ingresar en: if __name__ == "__main__":
nombrePokemon = input("Ingrese nombre del Pokémon: ")
buscarPokemon(nombrePokemon)

    
#2 - se escribre una funcion buscarPokemon ya que esta sera nuestro parámetro para busquemos
el nombre del Pokémon que queremos buscar en la PokeAPI y tambien y 
Se usa una f-string para construir la URL de la PokeAPI con el nombre del Pokémon 
url = f"https://pokeapi.co/api/v2/pokemon/{nombrePokemon.lower()}": 
Construye la URL para consultar en la pagina de PokeAPI

#3 - despues se hace una solicitud GET a la URL construida utilizando requests.get()
la respuesta de solisitud de la pagina de pokeaip 

#4 - y el  comando if response.status_code == 200: lo que va hacer es verificar
si la respuesta de la solicitud fue exitosa y si fue exitosa con el comando 
pokemon = response.json() onvierte la respuesta JSON de la PokeAPI en un diccionario de 
Python llamado "pokemon" y este diccionario tendra toda la informacion del pokemon que
tu desidise buscar

#5 - y el else pues en caso de cual quier error oh si la solisitud no fue exsitosa
se ejecutara y solo te mostrar que el pokemon no exsiste.

y ya.

"""