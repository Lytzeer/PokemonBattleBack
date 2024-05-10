from .pokemon_getter import get_random_pokemon, get_pokemon_stats, get_pokemon_id
from .pokeball_getter import get_pokeball_by_id
from .users_getter import get_user_id
from .move_getter import get_move_by_name
from random import randint

def opposant_pokemon(cur):
    data = get_random_pokemon(cur)
    pokemon ={}
    pokemon["name"] = data["name"]
    stats = get_pokemon_stats(cur, data["pokemon_id"])
    pokemon["stats"] = stats
    return pokemon

def get_user_pokeballs(cur, username):
    user_id = get_user_id(cur, username)
    cur.execute("SELECT pokeball_id, amount FROM user_pokeball WHERE user_id = ?", (user_id,))
    pokeballs = []
    for (pokeball_id, amount) in cur:
        pokeballs.append({"name": get_pokeball_by_id(cur, pokeball_id)["name"], "amount": amount})
    if len(pokeballs) == 0:
        return {"error": "User has no pokeballs"}
    return pokeballs

def check_pokeball_catch(cur, pokeball_name):
    cur.execute("SELECT catch_rate FROM pokeball WHERE name = ?", (pokeball_name,))
    catch_rate = cur.fetchone()[0]
    rnb = randint(1,100)
    return {"result": rnb <= catch_rate}

def match(cur,pokemon_name, attack_name, health, pokemon_name2, health2):
    pokemon1 = get_pokemon_stats(cur, get_user_id(cur, pokemon_name))
    pokemon2 = get_pokemon_stats(cur, get_user_id(cur, pokemon_name2))
    attack1 = get_move_by_name(cur, attack_name)
    opponent_id = get_pokemon_id(cur, pokemon_name2)
    opponent_attack = get_pokemon_stats(cur, opponent_id)
    attack2 = get_move_by_name(cur,opponent_attack["moves"][randint(0,3)]["name"])
    attack1_speed = attack1["speed"]
    attack2_speed = attack2["speed"]
    if attack1_speed > attack2_speed:
        health2 -= attack1["power"]
        if health2 <= 0:
            return {"winner": pokemon_name}
        health -= attack2["power"]
        if health <= 0:
            return {"winner": pokemon_name2}
    else:
        health -= attack2["power"]
        if health <= 0:
            return {"winner": pokemon_name2}
        health2 -= attack1["power"]
        if health2 <= 0:
            return {"winner": pokemon_name}
    return {"pokemon_health": health, "opponent_health": health2}
        

