from .pokemon_getter import get_random_pokemon, get_pokemon_stats, get_pokemon_types_by_id

def opposant_pokemon(cur):
    data = get_random_pokemon(cur)
    pokemon ={}
    pokemon["name"] = data["name"]
    stats = get_pokemon_stats(cur, data["pokemon_id"])
    pokemon["stats"] = stats
    return pokemon