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