def get_eggs(cur):
    cur.execute("SELECT * FROM eggs")
    egg_list = []
    for (egg_id, name, price) in cur:
        egg_list.append({"egg_id": egg_id, "name": name, "price": price})
    return egg_list