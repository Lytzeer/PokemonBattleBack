def get_standings(cur):
    cur.execute("SELECT username, money FROM users ORDER BY money DESC")
    standings = []
    i=1
    for (username, money) in cur:
        standings.append({"rank":i,"username": username, "money": money})
        i+=1
    return standings