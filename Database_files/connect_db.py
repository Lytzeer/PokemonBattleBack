import mariadb
import sys
from database_getter import get_pokemon,get_pokemon_by_id, get_move_by_id, get_pokemon_types_by_id, get_pokemon_moves, get_pokemon_types, get_pokemon_stats, get_pokedex_id_by_name, get_pokedex_id_by_pokemon_id, get_pokemon_id_by_name, get_type_by_id, get_type, get_move, get_pokemon_moves_by_id
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def connect():
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="127.0.0.1",
            port=3342,
            database="pokemon_battle"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    print("Connected to MariaDB Platform!")

    cur = conn.cursor()

    return cur

cur = connect()

@app.route('/pokemon')
def list_pokemon():
    pokemon=get_pokemon(cur)
    print(pokemon[0])
    return jsonify(pokemon)

@app.route('/pokemon/<int:pokemon_id>')
def list_pokemon_by_id(pokemon_id):
    pokemon=get_pokemon_by_id(cur, pokemon_id)
    return jsonify(pokemon)

@app.route('/move')
def list_move():
    move=get_move(cur)
    return jsonify(move)

@app.route('/move/<int:move_id>')
def list_move_by_id(move_id):
    move=get_move_by_id(cur, move_id)
    return jsonify(move)

@app.route('/pokemon/<int:pokemon_id>/move')
def list_pokemon_moves(pokemon_id):
    return jsonify(get_pokemon_moves_by_id(cur, pokemon_id))

@app.route('/pokemon/<int:pokemon_id>/type')
def list_pokemon_types(pokemon_id):
    return jsonify(get_pokemon_types_by_id(cur, pokemon_id))

if __name__ == '__main__':
    app.run()