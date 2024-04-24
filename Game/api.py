from Database_Connector.connect_db import connect
from Getter.pokemon_getter import get_pokemon, get_pokemon_by_id, get_pokemon_types_by_id, get_pokemon_moves_by_id, get_user_pokemon
from Getter.move_getter import get_move, get_move_by_id
from Getter.users_getter import get_user_info
from Getter.standing_getter import get_standings
from flask import Flask, jsonify, redirect
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return redirect('/pokemon', code=302)

@app.route('/pokemon')
@app.route('/pokemon/')
def list_pokemon():
    pokemon=get_pokemon(cur)
    return jsonify(pokemon), 200

@app.route('/pokemon/<int:pokemon_id>')
@app.route('/pokemon/<int:pokemon_id>/')
def list_pokemon_by_id(pokemon_id):
    pokemon=get_pokemon_by_id(cur, pokemon_id)
    return jsonify(pokemon), 200

@app.route('/move')
@app.route('/move/')
def list_move():
    move=get_move(cur)
    return jsonify(move), 200

@app.route('/move/<int:move_id>')
@app.route('/move/<int:move_id>/')
def list_move_by_id(move_id):
    move=get_move_by_id(cur, move_id)
    return jsonify(move), 200

@app.route('/pokemon/<int:pokemon_id>/move')
@app.route('/pokemon/<int:pokemon_id>/move/')
def list_pokemon_moves(pokemon_id):
    return jsonify(get_pokemon_moves_by_id(cur, pokemon_id)), 200

@app.route('/pokemon/<int:pokemon_id>/type')
@app.route('/pokemon/<int:pokemon_id>/type/')
def list_pokemon_types(pokemon_id):
    return jsonify(get_pokemon_types_by_id(cur, pokemon_id)), 200

@app.route('/user_pokemon/<int:user_id>')
@app.route('/user_pokemon/<int:user_id>/')
def list_user_pokemon(user_id):
    return jsonify(get_user_pokemon(cur, user_id)), 200

@app.route('/user_info/<string:username>')
@app.route('/user_info/<string:username>/')
def list_user_info(username):
    data = get_user_info(cur, username)
    if data == None:
        return jsonify({"error": "User not found"}), 404
    else:
        return {"username": username,"last_pokemon": data[0], "money": data[1], "standing_position": data[2]}

@app.route('/standing')
@app.route('/standing/')
def list_standing():
    return jsonify(get_standings(cur)), 200


if __name__ == '__main__':
    cur = connect()
    app.run(host='127.0.0.1', port=5000, debug=False)