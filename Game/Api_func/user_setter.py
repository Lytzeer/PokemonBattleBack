from .users_getter import get_user_id, get_money
from .pokeball_getter import get_pokeball_by_id
from .pokemon_getter import get_random_pokemon

def set_money(cur, username, money):
    user_id = get_user_id(cur, username)
    current_money = get_money(cur, username)
    cur.execute("UPDATE users SET money = %s WHERE id = %s", (current_money-money, user_id))
    return {"message": "Money updated successfully", "username": username, "money": current_money-money}

def set_user_buy_items(cur, username, amount, article, price):
    user_id = get_user_id(cur, username)
    if article == "Egg":
        set_money(cur, username, amount*price)
        pokemon=get_random_pokemon(cur)
        cur.execute("INSERT INTO user_pokemon (user_id, pokemon_id) VALUES (%s, %s)", (user_id, pokemon["pokemon_id"]))
        return {"message": "Egg bought successfully", "article": article, "amount": amount, "price": amount*price, "pokemon": pokemon["name"]}
    pokeball_id = get_pokeball_by_id(cur, article)["pokeball_id"]
    set_money(cur, username, amount*price)
    cur.execute("INSERT INTO user_pokeball (user_id, pokeball_id, amount) VALUES (%s, %s, %s)", (user_id, pokeball_id, amount))
    return {"message": "Pokeball bought successfully", "article": article, "amount": amount, "price": amount*price}