from flask import Flask,request
from main import insertUsuario

app = Flask(__name__)

@app.route("/return", methods=["GET"])
def retornoQualquer():
    return {'teste' : 'teste'}


@app.route("/request/response", methods=["POST"])
def recebeERetorna():
    return f'teste'


if (__name__ == '__main__'):
    app.run()