"""
API REST para el juego Ahorcado usando Flask.
"""

from flask import Flask, request, jsonify
from ahorcado_class import Ahorcado

app = Flask(__name__)
ahorcado = None # pylint: disable=invalid-name

@app.route('/saludo', methods=['POST'])
def saludo():
    """Saluda al usuario con el nombre dado en el parámetro 'nombre'."""
    nombre = request.args.get('nombre', 'desconocido')
    return f'Hola, {nombre}!'

@app.route('/getRightWord', methods=['GET'])
def getRightWord():
    """Devuelve la palabra correcta del juego actual."""
    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    return jsonify({'rightWord': ahorcado.getRightWord()})

@app.route('/getWordState', methods=['GET'])
def getWordState():
    """Devuelve el estado actual de la palabra (letras descubiertas)."""
    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    return jsonify({'wordState': ahorcado.getWordState()})

@app.route('/riskWord', methods=['POST'])
def riskWord():
    """Recibe una palabra arriesgada y devuelve si es correcta o no."""
    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    riskedWord = request.args.get('riskedWord', '')
    resultado = ahorcado.riskWord(riskedWord)
    return jsonify({'result': resultado})

@app.route('/riskedLetter', methods=['POST'])
def riskedLetter():
    """
    Recibe una letra arriesgada y devuelve:
    - True si está en la palabra,
    - False si no está,
    - "Game Over" si se acaban las vidas.
    """
    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    riskedLetters = request.args.get('riskedLetters', '').lower()
    resultado = ahorcado.riskLetter(riskedLetters)
    return jsonify({'result': resultado})

@app.route('/getRiskedLetters', methods=['GET'])
def getRiskedLetters():
    """Devuelve la lista de letras ya arriesgadas."""
    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    letras = list(ahorcado.getRiskedLetters())
    return jsonify({'riskedLetters': letras})

@app.route('/startGame', methods=['POST'])
def startGame():
    """Inicia un nuevo juego asignando una nueva palabra."""
    global ahorcado
    ahorcado = Ahorcado()
    return jsonify({'message': 'New Game Started'})

if __name__ == '__main__':
    app.run(debug=True)
