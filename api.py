from flask import Flask, request
from Ahorcado_class import Ahorcado

app = Flask(__name__)
ahorcado = Ahorcado()

#GET POST PUT DELETE

@app.route('/saludo', methods=['POST'])
def saludo():
    nombre = request.args.get('nombre', 'desconocido')
    return f'Hola, {nombre}!'

@app.route('/getRightWord', methods=['GET'])
def getRightWord():
    return ahorcado.getRightWord()


@app.route('/getWordState', methods=['GET'])
def getWordState():
    return ahorcado.getWordState()


@app.route('/riskWord', methods=['POST'])
def riskWord():
    riskedWord = request.args.get('riskedWord', '')
    return ahorcado.riskWord(riskedWord)



@app.route('/riskedLetter', methods=['POST'])
def riskedLetter():
    riskedLetter = request.args.get('riskedLetter', '')
    return ahorcado.riskWord(riskedLetter)



@app.route('/getRiskedLetters', methods=['GET'])
def getRiskedLetters():
    return ahorcado.getRiskedLetters()




if __name__ == '__main__':
    app.run(debug=True)
