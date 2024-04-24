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