from app import app
from flask import jsonify
# Criando rota na propria maquina, e pra interagir com o projeto WEB
# @ e um decorador


@app.route('/')
def raiz():
    return '123123world'


#Primeiro informa o tipo do parametro depois qual e o parametro e um parametro <string:nome> dentro da rota
@app.route('/pessoa/<string:nome>/<string:cidade>')
def pessoas(nome,cidade):
    #Utilizando Json
    return jsonify({'nome':nome, 'cidade': cidade})