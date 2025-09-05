##Banco de dados
from robotica_site import database
from flask_login import UserMixin
from datetime import datetime

class Noticias(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    descricao = database.Column(database.String, nullable = False)
    titulo = database.Column(database.String, nullable = False)
    link = database.Column(database.String, nullable = True, default = None)
    data_de_criacao = database.Column(database.DateTime, nullable = False, default =datetime.today())
    imagem = database.Column(database.String, nullable = False)

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    status = database.Column(database.Integer, default = 4, nullable = False)
    nome = database.Column(database.String, nullable = False)
    sobrenome = database.Column(database.String, nullable = False)
    email = database.Column(database.String, nullable = False, unique = True)
    senha = database.Column(database.String, nullable = False)
    imagem = database.Column(database.String, nullable = True, default = None)

class Projeto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    descricao = database.Column(database.String, nullable = False)
    titulo = database.Column(database.String, nullable = False)
    link = database.Column(database.String, nullable = True, default = None)
    imagem = database.Column(database.String, nullable = False)
    participantes = database.relationship('Usuario', backref='projeto', lazy= True)