from flask import Flask, request, jsonify
from Ahorcado_class import Ahorcado

app = Flask(__name__)
ahorcado = None

#GET POST PUT DELETE

@app.route('/saludo', methods=['POST'])
def saludo():
    nombre = request.args.get('nombre', 'desconocido')
    return f'Hola, {nombre}!'

@app.route('/getRightWord', methods=['GET'])
def getRightWord():

    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    
    return ahorcado.getRightWord()


@app.route('/getWordState', methods=['GET'])
def getWordState():

    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    
    return ahorcado.getWordState()


@app.route('/riskWord', methods=['POST'])
def riskWord():

    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    
    riskedWord = request.args.get('riskedWord', '')
    return str(ahorcado.riskWord(riskedWord))
    



@app.route('/riskedLetter', methods=['POST'])
def riskedLetter():

    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    
    riskedLetter = str(request.args.get('riskedLetter', '')).lower()

    return str(ahorcado.riskLetter(riskedLetter))




@app.route('/getRiskedLetters', methods=['GET'])
def getRiskedLetters():

    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    
    return str(ahorcado.getRiskedLetters())


@app.route('/startGame', methods=['POST'])
def startGame():
    global ahorcado
    ahorcado = Ahorcado()
    return 'New Game Started'


if __name__ == '__main__':
    app.run(debug=True)

