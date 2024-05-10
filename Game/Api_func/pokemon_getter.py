from .types_getter import get_type_by_id
from .move_getter import get_move_by_id
from random import randint

def get_pokemon(cur):
    cur.execute("SELECT * FROM pokemon")
    pokemon_list = []
    for (pokemon_id, pokedex_id, name, height, weight) in cur:
        pokemon_list.append({"pokemon_id": pokemon_id, "pokedex_id": pokedex_id, "name": name, "height": height, "weight": weight})
    return pokemon_list

def get_pokemon_id(cur, pokemon_name):
    cur.execute("SELECT pokemon_id FROM pokemon WHERE name = ?", (pokemon_name,))
    pokemon_id = cur.fetchone()
    return pokemon_id[0]

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

def get_random_pokemon(cur):
    cur.execute("SELECT COUNT(*) FROM pokemon")
    max_nb = cur.fetchone()[0]
    rnb = randint(1,max_nb)
    pokemon = get_pokemon_by_id(cur, rnb)
    return pokemon[0]

def get_pokemon_stats(cur, pokemon_id):
    cur.execute("SELECT * FROM stats WHERE pokemon_id = ?", (pokemon_id,))
    data = cur.fetchone()
    stats = {}
    stats["health"]= data[1]
    stats["attack"]= data[2]
    stats["defense"]= data[3]
    stats["spe_attack"]= data[4]
    stats["spe_defense"]= data[5]
    stats["speed"]= data[6]
    return stats