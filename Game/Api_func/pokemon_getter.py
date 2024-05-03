from .types_getter import get_type_by_id
from .move_getter import get_move_by_id
from random import randint

def get_pokemon(cur):
    cur.execute("SELECT * FROM pokemon")
    pokemon_list = []
    for (pokemon_id, pokedex_id, name, height, weight) in cur:
        pokemon_list.append({"pokemon_id": pokemon_id, "pokedex_id": pokedex_id, "name": name, "height": height, "weight": weight})
    return pokemon_list

def get_pokemon_by_id(cur, pokemon_id):
    cur.execute("SELECT * FROM pokemon WHERE pokemon_id = ?", (pokemon_id,))
    pokemon_list = []
    for (pokemon_id, pokedex_id, name, height, weight) in cur:
        pokemon_list.append({"pokemon_id": pokemon_id, "pokedex_id": pokedex_id, "name": name, "height": height, "weight": weight})
    return pokemon_list

def get_pokemon_types_by_id(cur, pokemon_id):
    cur.execute("SELECT type_id FROM pokemon_type WHERE pokemon_id = ?", (pokemon_id,))
    type_ids = cur.fetchall()
    types = []
    for (type_id,) in type_ids:
        ptype = get_type_by_id(cur, type_id)
        types.append(ptype)
    return types

def get_pokemon_moves_by_id(cur, pokemon_id):
    cur.execute("SELECT move_id FROM pokemon_move WHERE pokemon_id = ?", (pokemon_id,))
    move_ids = cur.fetchall()
    pokemon_moves = []
    for (move_id,) in move_ids:
        move = get_move_by_id(cur, move_id)
        pokemon_moves.append(move)
    return pokemon_moves

def get_user_pokemon(cur, user_id):
    cur.execute("SELECT user_id, pokemon_id FROM user_pokemon WHERE user_id = ?", (user_id,))
    user_pokemon = []
    for (user_id, pokemon_id) in cur:
        user_pokemon.append({"user_id": user_id, "pokemon_id": pokemon_id})
    return user_pokemon

def get_random_pokemon(cur):
    cur.execute("SELECT COUNT(*) FROM pokemon")
    max_nb = cur.fetchone()[0]
    rnb = randint(1,max_nb)
    pokemon = get_pokemon_by_id(cur, rnb)
    return pokemon[0]