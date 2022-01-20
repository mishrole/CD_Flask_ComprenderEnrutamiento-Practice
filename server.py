from flask import Flask

app = Flask(__name__)

@app.errorhandler(404)

def not_found(e):
    return "<p>¡Lo siento! No hay respuesta. Inténtalo otra vez</p>"

@app.route('/', methods=['GET'])
def index():
    return "<p>¡Hola Mundo!</p>"

@app.route('/dojo', methods=['GET'])
def dojo():
    return "<p>¡Dojo!</p>"

@app.route('/say/<name>', methods=['GET'])
def say(name):
    if not name.isnumeric():
        return "<p>¡Hola, {}!</p>".format(name)
    else:
        return "<p>¡Oops! No es una cadena</p>"

@app.route('/repeat/<id>/<name>', methods=['GET'])
def repeat(id, name):
    result = ""
    
    if not name.isnumeric() and id.isnumeric():
        for i in range(0, int(id)):
            result += f"<p>{name}</p>"
    else:
        if not id.isnumeric():
            result += f"<p>'{id}' debe ser un número"

        if name.isnumeric():
            result += f"<p>'{name}' debe ser una cadena</p>"
    
    return result

if __name__ == "__main__":
    app.run( debug = True )
