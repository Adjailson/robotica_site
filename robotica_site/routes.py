# Podemos usar apenas no final do projeto - Liandro
from flask import Flask, render_template, url_for, redirect
from robotica_site import app, database, bcrypt
from robotica_site.models import Usuario, Projeto, Membros, Noticias
from robotica_site.forms import FormCriarConta, FormLogin, FormMembroClube, FormNoticia, FormProjeto
from flask_login import login_required, login_user, logout_user, current_user

# Coloquei rotas para todos os arquivos html como teste. Ainda irei alterar essas rotas - Liandro
@app.route("/")
def index():
    return render_template('index.html')

#Testei o sistema de login e criar conta em um sistema mais simples e funcionou. O problema aqui é o banco de dados
@app.route("/login", methods = ['POST', 'GET'])
def login():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email = formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for("index"))
    return render_template("login.html", form=formlogin)

@app.route("/criarconta", methods = ['POST', 'GET'])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(email = formcriarconta.email.data, senha = senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("index"))
    return render_template("criarconta.html", form = formcriarconta)
'''
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
'''