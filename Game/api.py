from Database_Connector.connect_db import connect
from Api_func.pokemon_getter import get_pokemon, get_pokemon_by_id, get_pokemon_types_by_id, get_pokemon_moves_by_id, get_user_pokemon
from Api_func.move_getter import get_move, get_move_by_id
from Api_func.users_getter import get_user_info
from Api_func.standing_getter import get_standings
from Api_func.types_getter import get_type, get_type_by_id
from Api_func.pokeball_getter import get_pokeballs, get_max_pokeball_buyable
from Api_func.eggs_getter import get_max_egg_buyable, get_eggs
from Api_func.user_setter import set_user_buy_items
from Api_func.login_func import check_login, register_user
from flask import Flask, jsonify, redirect
from flask_cors import CORS
from json import load


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

@app.route('/type')
@app.route('/type/')
def list_type():
    return jsonify(get_type(cur)), 200

@app.route('/type/<int:type_id>')
@app.route('/type/<int:type_id>/')
def list_type_by_id(type_id):
    return jsonify(get_type_by_id(cur, type_id)), 200

@app.route('/buy/<string:username>/<string:articles>/<int:number>/<int:price>')
@app.route('/buy/<string:username>/<string:articles>/<int:number>/<int:price>/')
def buy_article(username, articles, number, price):
    return set_user_buy_items(cur, username, number, articles, price), 200

@app.route('/pokeball')
@app.route('/pokeball/')
def list_pokeball():
    return jsonify(get_pokeballs(cur)), 200

@app.route('/egg')
@app.route('/egg/')
def list_egg():
    return jsonify(get_eggs(cur)), 200

@app.route('/shop/<string:username>')
@app.route('/shop/<string:username>/')
def shop(username):
    return jsonify({"pokeballs": get_max_pokeball_buyable(cur, username), "eggs": get_max_egg_buyable(cur, username)}), 200

@app.route('/login/<string:username>/<string:password>')
@app.route('/login/<string:username>/<string:password>/')
def login(username, password):
    return jsonify(check_login(username, password)), 200

@app.route('/register/<string:username>/<string:password>/<string:password2>/<string:email>')
@app.route('/register/<string:username>/<string:password>/<string:password2>/<string:email>/')
def register(username, password, password2, email):
    return jsonify(register_user(username, password, password2, email)), 200


if __name__ == '__main__':
    cur = connect()
    with open('./Game/Config/api_conf.json', 'r') as file:
        config = load(file)
    app.run(host=config["host"], port=config["port"], debug=config["debug"])