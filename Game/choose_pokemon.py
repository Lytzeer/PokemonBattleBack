from requests import get
from random import randint
from connect_db import connect

def get_pokemon():
    response = get("http://localhost:5000/pokemon")
    return response.json()

def choose_pokemon():
    pokemon = get_pokemon()
    pokemon_list = []
    for i in range(4):
        rnb = randint(0, len(pokemon)-1)
        print(f"{i+1}: {pokemon[rnb]['name']}, ID: {pokemon[rnb]['pokemon_id']}")
        pokemon_list.append(pokemon[rnb])
    return pokemon_list

def set_pokemon_to_db(pokemon):
    cur = connect()
    for i in range(4):
        cur.execute("INSERT INTO user_pokemon (user_id, pokemon_id) VALUES (?,?)", (1,pokemon[i]['pokemon_id']))
    cur.connection.commit()
    cur.close()
    print("Pokemon added to database")

if __name__ == "__main__":
    pokemon = choose_pokemon()
    set_pokemon_to_db(pokemon)