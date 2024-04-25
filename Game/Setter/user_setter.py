from ..Getter.users_getter import get_user_id, get_money
from ..Getter.pokeball_getter import get_pokeball_id

def set_money(cur, username, money):
    user_id = get_user_id(cur, username)
    current_money = get_money(cur, username)
    cur.execute("UPDATE users SET money = %s WHERE id = %s", (current_money-money, user_id))
    return {"message": "Money updated successfully", "username": username, "money": current_money-money}

def set_user_buy_pokeball(cur, username, amount, article, price):
    user_id = get_user_id(cur, username)
    pokeball_id = get_pokeball_id(cur, article)
    set_money(cur, username, amount*price)
    cur.execute("INSERT INTO user_pokeball (user_id, pokeball_id, amount) VALUES (%s, %s, %s)", (user_id, pokeball_id, amount))
    return {"message": "Pokeball bought successfully", "article": article, "amount": amount, "price": amount*price}