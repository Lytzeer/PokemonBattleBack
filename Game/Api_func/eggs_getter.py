from .users_getter import get_money

def get_eggs(cur):
    cur.execute("SELECT * FROM eggs")
    egg_list = []
    for (egg_id, name, price) in cur:
        egg_list.append({"egg_id": egg_id, "name": name, "price": price})
    return egg_list

def get_max_egg_buyable(cur, username):
    money=get_money(cur, username)
    eggs=get_eggs(cur)
    egg_list=[]
    max_egg_buyable=0
    for egg in eggs:
        if egg["price"]<=money:
            max_egg_buyable=money//egg["price"]
        egg_list.append({"name": egg["name"], "price": egg["price"], "max_amount": max_egg_buyable})
        max_egg_buyable=0
    return egg_list
