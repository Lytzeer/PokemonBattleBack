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
    
def get_move_by_name(cur, move_name):
    cur.execute("SELECT * FROM move WHERE name = ?", (move_name,))
    for (move_id, name, category, power, pp, accuracy, priority, type_id) in cur:
        return {"move_id": move_id, "name": name, "category": category, "power": power, "pp": pp, "accuracy": accuracy, "priority": priority, "type_id": type_id}