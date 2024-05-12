from .pokemon_getter import get_pokemon_by_id, get_pokemon_types_by_id, get_pokemon_stats

def get_user_info(cur, username):
    cur.execute("SELECT user_id FROM users WHERE username = ?", (username,))
    user_id = cur.fetchone()
    info = []
    info.append(get_last_user_pokemon(cur, user_id[0]))
    cur.execute("SELECT money FROM users WHERE user_id = ?", (user_id[0],))
    money = cur.fetchone()
    info.append(money[0])
    standing_position = get_standing_index(cur, username)
    info.append(standing_position)
    return info

def get_last_user_pokemon(cur, user_id):
    user_pokemon = get_user_pokemon(cur, user_id)
    last_pokemons = []
    last_pokemons.append(user_pokemon[-1])
    last_pokemons.append(user_pokemon[-2])
    pokemon_infos = []
    for pokemon in last_pokemons:
        pokemon_info = get_pokemon_by_id(cur, pokemon["pokemon_id"])
        pokemon_type = get_pokemon_types_by_id(cur, pokemon["pokemon_id"])
        pokemon_info[0]["types"] = pokemon_type
        pokemon_infos.append(pokemon_info[0])
    return pokemon_infos

def get_user_id(cur, username):
    cur.execute("SELECT user_id FROM users WHERE username = ?", (username,))
    user_id = cur.fetchone()
    return user_id[0]

def get_all_users_info(cur):
    cur.execute("SELECT user_id, money FROM users")
    all_users = []
    for (user_id, money) in cur:
        all_users.append({"user_id": user_id, "money": money})
    return all_users

def get_standing_index(cur, username):
    user_id = get_user_id(cur, username)
    all_users = get_all_users_info(cur)
    index = find_index_user(all_users, user_id)
    if index == -1:
        return {"error": "User not found"}
    else:
        return index
    
def find_index_user(users, user_id):
    for i in range(len(users)):
        if users[i]["user_id"] == user_id:
            return i+1
    return -1

def get_money(cur, username):
    user_id = get_user_id(cur, username)
    cur.execute("SELECT money FROM users WHERE user_id = ?", (user_id,))
    money = cur.fetchone()
    return money[0]

def get_user_pokemon(cur, user_id):
    cur.execute("SELECT * FROM user_pokemon WHERE user_id = ?", (user_id,))
    user_pokemon = []
    for (user_pokemon_id, user_id, pokemon_id) in cur:
        user_pokemon.append({"user_pokemon_id": user_pokemon_id, "user_id": user_id, "pokemon_id": pokemon_id})
    return user_pokemon

def get_all_user_pokemon(cur, username):
    user_id = get_user_id(cur, username)
    user_pokemon = get_user_pokemon(cur, user_id)
    pokemon_list = []
    for pokemon in user_pokemon:
        pokemon_info = get_pokemon_by_id(cur, pokemon["pokemon_id"])
        pokemon_stats = get_pokemon_stats(cur, pokemon["pokemon_id"])
        pokemon_info[0]["stats"] = pokemon_stats
        pokemon_list.append(pokemon_info[0])
    return pokemon_list