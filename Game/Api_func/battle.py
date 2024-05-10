from .pokemon_getter import get_random_pokemon, get_pokemon_stats, get_pokemon_types_by_id

def opposant_pokemon(cur):
    data = get_random_pokemon(cur)
    pokemon_id = data["pokemon_id"]
    types = get_pokemon_types_by_id(cur, pokemon_id)
    types_data = {}
    if len(types) > 1:
        types_data["type1"] = types[0][0]["name"]
        types_data["type2"] = types[1][0]["name"]
    else:
        types_data["type1"] = types[0][0]["name"]
    pokemon ={}
    pokemon["name"] = data["name"]
    stats = get_pokemon_stats(cur, data["pokemon_id"])
    pokemon["stats"] = stats
    pokemon["types"] = types_data
    return pokemon