import bcrypt
import json
from random import randint
from .users_getter import get_user_id
from .pokemon_getter import get_pokemon

def check_login(cur, username, password):
    cur.execute("SELECT * FROM users WHERE username = ? ", (username,))
    user = cur.fetchone()
    if user == None:
        return {"message": False}
    else:
        salt = get_salt().encode('utf-8')
        bytes_password = password.encode('utf-8')
        hash = bcrypt.hashpw(bytes_password, salt)
        if user[3].encode('utf-8') == hash:
            return {"message": True}
        else:
            return {"message": False}
        
def register_user(cur, username, password, password2, email):
    if password != password2:
        return {"message": False, "error": "Passwords do not match"}
    else:
        cur.execute("SELECT username FROM users WHERE username = ?", (username,))
        user = cur.fetchone()
        if user != None:
            return {"message": False, "error": "Username already exists"}
        else:
            salt = get_salt().encode('utf-8')
            bytes_password = password.encode('utf-8')
            hash = bcrypt.hashpw(bytes_password, salt)
            cur.execute("INSERT INTO users (username, password, email, money) VALUES (?, ?, ?, 0)", (username, hash, email))
            cur.connection.commit()
            user_id = get_user_id(cur, username)
            pokemon = choose_pokemon(cur)
            for i in range(4):
                cur.execute("INSERT INTO user_pokemon (user_id, pokemon_id) VALUES (?,?)", (user_id,pokemon[i]['pokemon_id']))
            cur.connection.commit()
            return {"message": True}
        
def get_salt():
    with open('./Game/Config/api_conf.json', 'r') as file:
        data = json.load(file)
    return data["seed"]

def choose_pokemon(cur):
    pokemon = get_pokemon(cur)
    pokemon_list = []
    for i in range(4):
        rnb = randint(0, len(pokemon)-1)
        print(f"{i+1}: {pokemon[rnb]['name']}, ID: {pokemon[rnb]['pokemon_id']}")
        pokemon_list.append(pokemon[rnb])
    return pokemon_list