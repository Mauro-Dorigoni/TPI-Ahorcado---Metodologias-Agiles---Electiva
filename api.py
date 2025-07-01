from flask import Flask, request, jsonify
from Ahorcado_class import Ahorcado

app = Flask(__name__)
ahorcado = None

#GET POST PUT DELETE

@app.route('/saludo', methods=['POST'])
def saludo():
    nombre = request.args.get('nombre', 'desconocido')
    return f'Hola, {nombre}!'

#GET --> RETURN RIGHT WORD 
@app.route('/getRightWord', methods=['GET'])
def getRightWord():

    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    
    return ahorcado.getRightWord()


#GET --> RETURN STATE OF THE WORD. EXAMPLE: L A U _ A R _
@app.route('/getWordState', methods=['GET'])
def getWordState():

    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    
    return ahorcado.getWordState()


#POST --> RECIBE A WORD TO RISK IN AN ARGUMENT. RETURN TRUE OR FALSE IF IS NOT CORRECT.
#EXAMPLE /riskWord?riskedWord=melon
@app.route('/riskWord', methods=['POST'])
def riskWord():

    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    
    riskedWord = request.args.get('riskedWord', '')
    return str(ahorcado.riskWord(riskedWord))
    


#POST --> RECIBE A LETTER TO RISK IN AN ARGUMENT. RETURN TRUE OR FALSE IF IS NOT CORRECT. RETURN GAME OVER IF LIVES = 0
# CA: ¿Puede ser mala practica que una función devuelva dos tipos de datos distintos? (Tecnicamente son todos string, pero...)
#EXAMPLE /riskedLetter?riskedLetter=m
@app.route('/riskedLetter', methods=['POST'])
def riskedLetter():

    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    
    riskedLetter = str(request.args.get('riskedLetter', '')).lower()

    return str(ahorcado.riskLetter(riskedLetter))



#GET --> RETURN A LIST WITH RISKED LETTERS 
@app.route('/getRiskedLetters', methods=['GET'])
def getRiskedLetters():

    if ahorcado is None:
        return jsonify({'error': 'No hay juego iniciado'}), 400
    
    return str(ahorcado.getRiskedLetters())


#POST --> START A GAME. ASSING A NEW WORD EVERY TIME IS CALLED.
@app.route('/startGame', methods=['POST'])
def startGame():
    global ahorcado
    ahorcado = Ahorcado()
    return 'New Game Started'

#ONLY SUPPORT SINGLE PLAYER. 
if __name__ == '__main__':
    app.run(debug=True)

