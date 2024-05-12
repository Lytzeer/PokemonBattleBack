from .pokemon_getter import get_random_pokemon, get_pokemon_stats, get_pokemon_id
from .pokeball_getter import get_pokeball_by_id
from .users_getter import get_user_id
from .user_setter import add_money
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
    print(username)
    user_id = get_user_id(cur, username)
    print(user_id)
    cur.execute("SELECT DISTINCT pokeball_id, amount FROM user_pokeball WHERE user_id = ?", (user_id,))
    rows = cur.fetchall()
    pokeballs = []
    for (pokeball_id, amount) in rows:
        print(pokeball_id)
        pokeballs.append({"name": get_pokeball_by_id(cur, pokeball_id)["name"], "amount": amount})
    if len(pokeballs) == 0:
        return {"error": "User has no pokeballs"}
    return pokeballs

def check_pokeball_catch(cur, pokeball_name):
    cur.execute("SELECT catch_rate FROM pokeball WHERE name = ?", (pokeball_name,))
    catch_rate = cur.fetchone()[0]
    rnb = randint(1,100)
    return {"result": rnb <= catch_rate}

def match(cur,username, attack_name, health, pokemon_name2, health2):
    attack1 = get_move_by_name(cur, attack_name)
    opponent_id = get_pokemon_id(cur, pokemon_name2)
    opponent_attack = get_pokemon_stats(cur, opponent_id)
    attack2 = opponent_attack["moves"][randint(0, len(opponent_attack["moves"])-1)]
    attack1_speed = attack1["priority"]
    attack2_speed = attack2["priority"]
    if attack2["power"] == None:
        attack2["power"] = 50
    if attack1_speed > attack2_speed:
        health2 -= round(attack1["power"]/2.5)
        if health2 <= 0:
            add_money(cur, username, 1500)
            return {"winner": "Player", "opponent_health": 0, "pokemon_health": health}
        health -= round(attack2["power"]/2.5)
        if health <= 0:
            return {"winner": "Trainer", "opponent_health": health2, "pokemon_health": 0}
    else:
        health -= round(attack2["power"]/2.5)
        if health <= 0:
            return {"winner": "Trainer", "opponent_health": health2, "pokemon_health": 0}
        health2 -= round(attack1["power"]/2.5)
        if health2 <= 0:
            add_money(cur, username, 1500)
            return {"winner": "Player", "opponent_health": 0, "pokemon_health": health}
    return {"pokemon_health": health, "opponent_health": health2}
        

