
#REST API for the hangman game, using the hangban class.

from flask import Flask, request, jsonify
from flask_cors import CORS
from ahorcado_class import Ahorcado
from dotenv import load_dotenv
import os
from flask import session
from uuid import uuid4


#env_file = os.environ.get("APP_ENV_FILE", ".env")

environment = os.getenv("FLASK_ENV")
debug_mode = True if environment == "development" else False
testing = False 

app = Flask(__name__)

app.config.update(
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True
)

CORS(app, supports_credentials=True, origins=["https://tpi-ahorcado-metodologias-agiles-el.vercel.app","http://localhost:3000"])
#ahorcado = None # pylint: disable=invalid-name

app.secret_key = os.getenv("SECRET_KEY", "clave-super-secreta")

# Diccionario global de juegos
games = {}

# Middleware para asegurar que cada cliente tenga un session_id
@app.before_request
def ensure_session():
#    session['testMode'] = False
    if 'session_id' not in session:
        session['session_id'] = str(uuid4())

# Función auxiliar para obtener el juego actual
def get_current_game():
    session_id = session.get('session_id')
    return games.get(session_id)

# Función auxiliar para establecer el juego actual
def set_current_game(game_instance):
    session_id = session.get('session_id')
    games[session_id] = game_instance

#----------------------------------------------------------------------

@app.route('/saludo', methods=['POST'])
def saludo():
    #Greets the user. Purely for debugging purposes.
    nombre = request.args.get('nombre', 'desconocido')
    return f'Hola, {nombre}!'

@app.route('/getRightWord', methods=['GET'])
def getRightWord():
    #Returns the right word for the current game
    game = get_current_game()
    if game is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    return jsonify({'rightWord': game.getRightWord()})

@app.route('/getWordState', methods=['GET'])
def getWordState():
    #Returns the current state of the palayers gueses (right letters discovered)
    game = get_current_game()
    if game is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    return jsonify({'wordState': game.getWordState()})

@app.route('/riskWord', methods=['POST'])
def riskWord():
    #Recieves a risked word and returns true or false.
    game = get_current_game()
    if game is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    riskedWord = request.args.get('riskedWord', '')
    resultado = game.riskWord(riskedWord)
    return jsonify({'result': resultado})

@app.route('/riskedLetter', methods=['POST'])
def riskedLetter():
    """
    Recieves a risked letter and returns:
    - Trueif the letter is in the right word,
    - False if its not,
    - "Game Over" if the player is out of lives.
    """
    game = get_current_game()
    if game is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    riskedLetters = request.args.get('riskedLetters', '').lower()
    resultado = game.riskLetter(riskedLetters)
    return jsonify({'result': resultado})

@app.route('/getRiskedLetters', methods=['GET'])
def getRiskedLetters():
    #Returns the list of risked letter by the player
    game = get_current_game()
    if game is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    letras = list(game.getRiskedLetters())
    return jsonify({'riskedLetters': letras})

@app.route('/startGame', methods=['POST'])
def startGame():

    set_current_game(Ahorcado(testMode=testing))
    return jsonify({'message': 'New Game Started'})



if __name__ == '__main__':
    app.run(debug=debug_mode, host='0.0.0.0', port=10000)
