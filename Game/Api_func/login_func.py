import bcrypt
import json

def check_login(cur, username, password):
    cur.execute("SELECT * FROM users WHERE username = ? ", (username,))
    user = cur.fetchone()
    if user == None:
        return {"message": False}
    else:
        salt = get_salt()
        bytes_password = password.encode('utf-8')
        hash = bcrypt.hashpw(bytes_password, salt)
        if bcrypt.checkpw(user[2].encode('utf-8'), hash):
            return {"message": True}
        else:
            return {"message": False}
        
def register_user(cur, username, password, password2, email):
    if password != password2:
        return {"message": False, "error": "Passwords do not match"}
    else:
        cur.execute("SELECT username FROM users WHERE username = ?", (username,))
        user = cur.fetchone()
        if user != None:
            return {"message": False, "error": "Username already exists"}
        else:
            salt = get_salt()
            bytes_password = password.encode('utf-8')
            hash = bcrypt.hashpw(bytes_password, salt)
            cur.execute("INSERT INTO users (username, password, email, money) VALUES (?, ?, ?, 0)", (username, hash, email))
            cur.connection.commit()
            return {"message": True}
        
def get_salt():
    with open('./Game/Config/api_conf.json', 'r') as file:
        data = json.load(file)
    return data["seed"]