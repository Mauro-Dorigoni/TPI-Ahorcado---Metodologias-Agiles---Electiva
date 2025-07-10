
#REST API for the hangman game, using the hangban class.

from flask import Flask, request, jsonify
from flask_cors import CORS
from ahorcado_class import Ahorcado
from dotenv import load_dotenv
import os

load_dotenv()

environment = os.getenv("FLASK_ENV")
if(environment == "development"):
    debug_mode = True
else:
    debug_mode = False

app = Flask(__name__)
CORS(app)
ahorcado = None # pylint: disable=invalid-name

@app.route('/saludo', methods=['POST'])
def saludo():
    #Greets the user. Purely for debugging purposes.
    nombre = request.args.get('nombre', 'desconocido')
    return f'Hola, {nombre}!'

@app.route('/getRightWord', methods=['GET'])
def getRightWord():
    #Returns the right word for the current game
    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    return jsonify({'rightWord': ahorcado.getRightWord()})

@app.route('/getWordState', methods=['GET'])
def getWordState():
    #Returns the current state of the palayers gueses (right letters discovered)
    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    return jsonify({'wordState': ahorcado.getWordState()})

@app.route('/riskWord', methods=['POST'])
def riskWord():
    #Recieves a risked word and returns true or false.
    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    riskedWord = request.args.get('riskedWord', '')
    resultado = ahorcado.riskWord(riskedWord)
    return jsonify({'result': resultado})

@app.route('/riskedLetter', methods=['POST'])
def riskedLetter():
    """
    Recieves a risked letter and returns:
    - Trueif the letter is in the right word,
    - False if its not,
    - "Game Over" if the player is out of lives.
    """
    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    riskedLetters = request.args.get('riskedLetters', '').lower()
    resultado = ahorcado.riskLetter(riskedLetters)
    return jsonify({'result': resultado})

@app.route('/getRiskedLetters', methods=['GET'])
def getRiskedLetters():
    #Returns the list of risked letter by the player
    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    letras = list(ahorcado.getRiskedLetters())
    return jsonify({'riskedLetters': letras})

@app.route('/startGame', methods=['POST'])
def startGame():
    #Starts a new hangman game
    global ahorcado # pylint: disable=global-statement
    ahorcado = Ahorcado()
    return jsonify({'message': 'New Game Started'})

if __name__ == '__main__':
    app.run(debug=debug_mode, host='0.0.0.0', port=10000)
