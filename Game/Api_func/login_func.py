import bcrypt

def check_login(cur, username, password):
    cur.execute("SELECT * FROM users WHERE username = ? ", (username,))
    user = cur.fetchone()
    if user == None:
        return {"message": False}
    else:
        bytes_password = password.encode('utf-8')
        hash = bcrypt.hashpw(bytes_password)
        if bcrypt.checkpw(user[2], hash):
            return {"message": True}
        else:
            return {"message": False}
        
def register(cur, username, password, password2, email):
    if password != password2:
        return {"message": False, "error": "Passwords do not match"}
    else:
        cur.execute("SELECT username FROM users WHERE username = ?", (username,))
        user = cur.fetchone()
        if user != None:
            return {"message": False, "error": "Username already exists"}
        else:
            bytes_password = password.encode('utf-8')
            hash = bcrypt.hashpw(bytes_password)
            cur.execute("INSERT INTO users (username, password, email, money) VALUES (?, ?, ?, 0)", (username, hash, email))
            cur.connection.commit()
            return {"message": True}