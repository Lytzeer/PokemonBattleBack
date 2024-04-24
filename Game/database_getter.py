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
    


def get_move(cur):
    cur.execute("SELECT * FROM move")
    move_list = []
    for (move_id, name, category, power, pp, accuracy, priority, type_id) in cur:
        move_list.append({"move_id": move_id, "name": name, "category": category, "power": power, "pp": pp, "accuracy": accuracy, "priority": priority, "type_id": type_id})
    return move_list


def get_move_by_id(cur, move_id):
    if move_id == 0:
        print("Invalid move ID")
        return
    cur.execute("SELECT * FROM move WHERE move_id = ?", (move_id,))
    for (move_id, name, category, power, pp, accuracy, priority, type_id) in cur:
        return {"move_id": move_id, "name": name, "category": category, "power": power, "pp": pp, "accuracy": accuracy, "priority": priority, "type_id": type_id}


def get_pokemon_moves(cur, pokemon_id,slot):
    cur.execute("SELECT pokemon_id,move_id FROM pokemon_move WHERE pokemon_id = ? AND slot = ?", (pokemon_id,slot))
    pokemon_moves = []
    for (pokemon_id, move_id) in cur:
        move = get_move_by_id(cur, move_id)
        pokemon_moves.append(move)
    return pokemon_moves


def get_pokemon_moves_by_id(cur, pokemon_id):
    cur.execute("SELECT move_id FROM pokemon_move WHERE pokemon_id = ?", (pokemon_id,))
    move_ids = cur.fetchall()
    pokemon_moves = []
    for (move_id,) in move_ids:
        move = get_move_by_id(cur, move_id)
        pokemon_moves.append(move)
    return pokemon_moves


def get_pokemon_types(cur, pokemon_id, slot):
    cur.execute("SELECT pokemon_id,type_id FROM pokemon_type WHERE pokemon_id = ? AND slot = ?", (pokemon_id,slot))
    for (pokemon_id, type_id) in cur:
        print(f"Pokemon ID: {pokemon_id}, {get_type_by_id(cur, type_id)}")

def get_pokemon_types_by_id(cur, pokemon_id):
    cur.execute("SELECT type_id FROM pokemon_type WHERE pokemon_id = ?", (pokemon_id,))
    type_ids = cur.fetchall()
    types = []
    for (type_id,) in type_ids:
        type = get_type_by_id(cur, type_id)
        types.append(type)
    return types


def get_type_by_id(cur, type_id):
    cur.execute("SELECT * FROM type WHERE type_id = ?", (type_id,))
    types = []
    for (type_id, name) in cur:
        types.append({"type_id": type_id, "name": name})
    return types


def get_type(cur):
    cur.execute("SELECT * FROM type")
    type_list = []
    for (type_id, name) in cur:
        type_list.append({"type_id": type_id, "name": name})
    return type_list


def get_pokemon_stats(cur, pokemon_id):
    cur.execute("SELECT * FROM stats WHERE pokemon_id = ?", (pokemon_id,))
    for (stat_id, health, attack, defense, spe_attack, spe_defense, speed, pokemon_id) in cur:
        print(f"Stat ID : {stat_id}, Pokemon ID: {pokemon_id}, HP: {health}, Attack: {attack}, Defense: {defense}, Special Attack: {spe_attack}, Special Defense: {spe_defense}, Speed: {speed}")
        return {"health": health, "attack": attack, "defense": defense, "special_attack": spe_attack, "special_defense": spe_defense, "speed": speed}


def get_pokemon_id_by_name(cur, name):
    cur.execute("SELECT * FROM pokemon WHERE name = ?", (name,))
    for (pokemon_id, pokedex_id, name, height, weight) in cur:
        print(f"Pokemon ID: {pokemon_id}, Name: {name}, Pokedex ID: {pokedex_id}, Height: {height}, Weight: {weight}")
        return {"pokemon_id": pokemon_id, "name": name, "pokedex_id": pokedex_id, "height": height, "weight": weight}


def get_pokedex_id_by_name(cur, name):
    cur.execute("SELECT pokedex_id, name FROM pokemon WHERE name = ?", (name,))
    for (pokedex_id, name) in cur:
        print(f"Pokedex ID: {pokedex_id}, Name: {name}")
        return {"pokedex_id": pokedex_id, "name": name}


def get_pokedex_id_by_pokemon_id(cur, pokemon_id):
    cur.execute("SELECT pokedex_id, name FROM pokemon WHERE pokemon_id = ?", (pokemon_id,))
    for (pokedex_id, name) in cur:
        print(f"Pokedex ID: {pokedex_id}, Name: {name}")
        return {"pokedex_id": pokedex_id, "name": name}
    
def get_user_pokemon(cur, user_id):
    cur.execute("SELECT user_id, pokemon_id FROM user_pokemon WHERE user_id = ?", (user_id,))
    user_pokemon = []
    for (user_id, pokemon_id) in cur:
        user_pokemon.append({"user_id": user_id, "pokemon_id": pokemon_id})
    return user_pokemon

def get_last_user_pokemon(cur, user_id):
    user_pokemon = get_user_pokemon(cur, user_id)
    last_pokemons = []
    last_pokemons.append(user_pokemon[-1])
    last_pokemons.append(user_pokemon[-2])
    return last_pokemons

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

def find_index_user(users, user_id):
    for i in range(len(users)):
        if users[i]["user_id"] == user_id:
            return i+1
    return -1

def get_standing_index(cur, username):
    user_id = get_user_id(cur, username)
    all_users = get_all_users_info(cur)
    index = find_index_user(all_users, user_id)
    if index == -1:
        return {"error": "User not found"}
    else:
        return index
