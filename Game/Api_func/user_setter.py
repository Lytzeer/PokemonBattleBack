from .users_getter import get_user_id, get_money
from .pokeball_getter import get_pokeball_by_name
from .pokemon_getter import get_random_pokemon

def set_money(cur, username, money):
    user_id = get_user_id(cur, username)
    current_money = get_money(cur, username)
    cur.execute("UPDATE users SET money = %s WHERE user_id = %s", (current_money-money, user_id))
    cur.commit()
    return {"message": "Money updated successfully", "username": username, "money": current_money-money}

def set_user_buy_items(cur, username, amount, article, price):
    user_id = get_user_id(cur, username)
    if article == "Egg":
        set_money(cur, username, amount*price)
        pokemon=get_random_pokemon(cur)
        cur.execute("INSERT INTO user_pokemon (user_id, pokemon_id) VALUES (%s, %s)", (user_id, pokemon["pokemon_id"]))
        cur.commit()
        return {"message": "Egg bought successfully", "article": article, "amount": amount, "price": amount*price, "pokemon": pokemon["name"]}
    pokeball = get_pokeball_by_name(cur, article)
    set_money(cur, username, amount*price)
    cur.execute("INSERT INTO user_pokeball (user_id, pokeball_id, amount) VALUES (%s, %s, %s)", (user_id, pokeball["pokeball_id"], amount))
    cur.commit()
    return {"message": "Pokeball bought successfully", "article": article, "amount": amount, "price": amount*price}