from .users_getter import get_money

def get_pokeballs(cur):
    cur.execute("SELECT * FROM pokeball")
    pokeball_list = []
    for (pokeball_id, name, catch_rate, price) in cur:
        pokeball_list.append({"pokeball_id": pokeball_id, "name": name, "catch_rate": catch_rate, "price": price})
    return pokeball_list

def get_pokeball_by_id(cur, pokeball_id):
    if pokeball_id == 0:
        print("Invalid pokeball ID")
        return
    cur.execute("SELECT * FROM pokeball WHERE pokeball_id = ?", (pokeball_id,))
    for (pokeball_id, name, catch_rate, price) in cur:
        return {"pokeball_id": pokeball_id, "name": name, "catch_rate": catch_rate, "price": price}
    
def get_pokeball_by_name(cur, pokeball_name):
    cur.execute("SELECT * FROM pokeball WHERE name = ?", (pokeball_name,))
    for (pokeball_id, name, catch_rate, price) in cur:
        return {"pokeball_id": pokeball_id, "name": name, "catch_rate": catch_rate, "price": price}

def get_max_pokeball_buyable(cur, username):
    money=get_money(cur, username)
    pokeballs=get_pokeballs(cur)
    pokeball_list=[]
    max_pokeball_buyable=0
    for pokeball in pokeballs:
        if pokeball["price"]<=money:
            max_pokeball_buyable=money//pokeball["price"]
        pokeball_list.append({"name": pokeball["name"], "price": pokeball["price"], "max_amount": max_pokeball_buyable})
        max_pokeball_buyable=0
    return pokeball_list