from Database_Connector.connect_db import connect
from Api_func.pokemon_getter import get_pokemon, get_pokemon_by_id, get_pokemon_types_by_id, get_pokemon_moves_by_id, get_pokemon_id, get_pokemon_stats
from Api_func.move_getter import get_move, get_move_by_id
from Api_func.users_getter import get_user_info, get_all_user_pokemon
from Api_func.standing_getter import get_standings
from Api_func.types_getter import get_type, get_type_by_id
from Api_func.pokeball_getter import get_pokeballs, get_max_pokeball_buyable
from Api_func.eggs_getter import get_max_egg_buyable, get_eggs
from Api_func.user_setter import set_user_buy_items, set_new_username, set_new_password, delete_user, set_catched_pokemon
from Api_func.login_func import check_login, register_user
from Api_func.battle import opposant_pokemon, get_user_pokeballs, check_pokeball_catch, match
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

@app.route('/user_pokemon/<string:username>')
@app.route('/user_pokemon/<string:username>/')
def list_user_pokemon(username):
    return jsonify(get_all_user_pokemon(cur, username)), 200

@app.route('/user_info/<string:username>')
@app.route('/user_info/<string:username>/')
def list_user_info(username):
    data = get_user_info(cur, username)
    if data == None:
        return jsonify({"error": "User not found"}), 404
    else:
        return {"username": username,"last_pokemon": data[0], "money": data[1], "standing_position": data[2]}
    
@app.route('/user_info/<string:username>/update_username/<string:new_username>')
@app.route('/user_info/<string:username>/update_username/<string:new_username>/')
def update_username(username, new_username):
    return jsonify(set_new_username(cur, username, new_username)), 200

@app.route('/user_info/<string:username>/update_password/<string:new_password>')
@app.route('/user_info/<string:username>/update_password/<string:new_password>/')
def update_password(username, new_password):
    return jsonify(set_new_password(cur, username, new_password)), 200

@app.route('/user_info/<string:username>/delete')
@app.route('/user_info/<string:username>/delete/')
def delete(username):
    return jsonify(delete_user(cur, username)), 200

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
    return jsonify(check_login(cur, username, password)), 200

@app.route('/register/<string:username>/<string:password>/<string:password2>/<string:email>')
@app.route('/register/<string:username>/<string:password>/<string:password2>/<string:email>/')
def register(username, password, password2, email):
    return jsonify(register_user(cur, username, password, password2, email)), 200


@app.route('/random_opponent')
@app.route('/random_opponent/')
def random_opponent():
    return jsonify(opposant_pokemon(cur)), 200

@app.route('/pokemon_stats/<string:pokemon_name>')
@app.route('/pokemon_stats/<string:pokemon_name>/')
def pokemon_stats(pokemon_name):
    pokemon_id=get_pokemon_id(cur, pokemon_name)
    return jsonify(get_pokemon_stats(cur, pokemon_id)), 200

@app.route('/battle/<string:username>/<string:attack_name>/<int:health>/<string:pokemon_name2>/<int:health2>')
@app.route('/battle/<string:username>/<string:attack_name>/<int:health>/<string:pokemon_name2>/<int:health2>/')
def battle(username, attack_name, health, pokemon_name2, health2):
    return jsonify(match(cur,username, attack_name, health, pokemon_name2, health2)), 200

@app.route('/battle/pokeball/<string:username>')
@app.route('/battle/pokeball/<string:username>/')
def battle_pokeball(username):
    return jsonify(get_user_pokeballs(cur, username)), 200

@app.route('/battle/<string:pokeball_name>')
@app.route('/battle/<string:pokeball_name>/')
def catch(pokeball_name):
    return jsonify(check_pokeball_catch(cur, pokeball_name)), 200

@app.route('/battle/catched/<string:username>/<string:pokemon_name>')
@app.route('/battle/catched/<string:username>/<string:pokemon_name>/')
def catched(username, pokemon_name):
    return jsonify(set_catched_pokemon(cur, username, pokemon_name)), 200


if __name__ == '__main__':
    cur = connect()
    with open('./Game/Config/api_conf.json', 'r') as file:
        config = load(file)
    app.run(host=config["host"], port=config["port"], debug=config["debug"])