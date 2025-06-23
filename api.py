from flask import Flask, request

app = Flask(__name__)

@app.route('/saludo', methods=['POST'])
def saludo():
    nombre = request.args.get('nombre', 'desconocido')
    return f'Hola, {nombre}!'

@app.route('/holamundo', methods=['GET'])
def holamundo():
    return 'Hola Amigo'

if __name__ == '__main__':
    app.run()
