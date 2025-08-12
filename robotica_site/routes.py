# Podemos usar apenas no final do projeto - Liandro
from flask import Flask, render_template, url_for
from robotica_site import app

# Coloquei rotas para todos os arquivos html como teste. Ainda irei alterar essas rotas - Liandro
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/espaço-maker')
def espaco():
    return render_template('espaco_maker.html')
