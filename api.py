""" REST API for the hangman game, using the Ahorcado class. """

import os
from uuid import uuid4
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from dotenv import load_dotenv
from ahorcado_class import Ahorcado

env_name = os.getenv("ENVIRONMENT", "development")
if env_name == "production":
    load_dotenv(".env.production")
elif env_name == "testing":
    load_dotenv(".env.testing")
else:
    load_dotenv(".env.development")

environment = os.getenv("FLASK_ENV")
DEBUG_MODE = DEBUG_MODE = environment == "development"
testing = os.getenv("TESTING", "False").lower() == "true"

app = Flask(__name__)

app.config.update(
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True
)

CORS(app, supports_credentials=True, origins=["https://tpi-ahorcado-metodologias-agiles-el.vercel.app","http://localhost:3000"])

app.secret_key = os.getenv("SECRET_KEY", "clave-super-secreta")

# Global Game Diccionary
games = {}

# Middleware that ensures every user has an identifier
@app.before_request
def ensureSession():
    """ Method that ensures the session cookie is present """
    if 'sessionId' not in session:
        session['sessionId'] = str(uuid4())

def getCurrentGame():
    # Method that returns the current game
    sessionId = session.get('sessionId')
    return games.get(sessionId)

def setCurrentGame(gameInstance):
    """ Method that sets a current game """
    sessionId = session.get('sessionId')
    games[sessionId] = gameInstance

#----------------------------------------------------------------------

@app.route('/saludo', methods=['POST'])
def saludo():
    """ Greets the user. Purely for debugging purposes. """
    nombre = request.args.get('nombre', 'desconocido')
    return f'Hola, {nombre}!'

@app.route('/getRightWord', methods=['GET'])
def getRightWord():
    """ Returns the right word for the current game """
    game = getCurrentGame()
    if game is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    return jsonify({'rightWord': game.getRightWord()})

@app.route('/getWordState', methods=['GET'])
def getWordState():
    """ Returns the current state of the palayers gueses (right letters discovered) """
    game = getCurrentGame()
    if game is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    return jsonify({'wordState': game.getWordState()})

@app.route('/riskWord', methods=['POST'])
def riskWord():
    """ Recieves a risked word and returns true or false. """
    game = getCurrentGame()
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
    game = getCurrentGame()
    if game is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    riskedLetters = request.args.get('riskedLetters', '').lower()
    resultado = game.riskLetter(riskedLetters)
    return jsonify({'result': resultado})

@app.route('/getRiskedLetters', methods=['GET'])
def getRiskedLetters():
    """ Returns the list of risked letter by the player """
    game = getCurrentGame()
    if game is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    letras = list(game.getRiskedLetters())
    return jsonify({'riskedLetters': letras})

@app.route('/startGame', methods=['POST'])
def startGame():
    """ Starts a new game """
    setCurrentGame(Ahorcado(testMode=testing))
    return jsonify({'message': 'New Game Started'})



if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, host='0.0.0.0', port=10000)
