##Banco de dados
#Poblema serissimo com relação de tabelas diferentes de N:N e 1:1. Ainda a corrigir
from robotica_site import database, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_usuario(id):
    return Usuario.query.get(int(id))

class Noticias(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    descricao = database.Column(database.String, nullable = False)
    titulo = database.Column(database.String, nullable = False)
    link = database.Column(database.String, nullable = True, default = None)
    data_de_criacao = database.Column(database.DateTime, nullable = False, default = datetime.today())
    imagem = database.Column(database.String, nullable = False)

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    status = database.Column(database.Integer, default = 4, nullable = False)
    email = database.Column(database.String, nullable = False, unique = True)
    senha = database.Column(database.String, nullable = False)
    conta = database.relationship('Membros', backref='membros', lazy= True)

class Membros(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable = True)
    sobrenome = database.Column(database.String, nullable = True)
    imagem = database.Column(database.String, nullable = True, default = None)
    descricao = database.Column(database.String, nullable = True)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id') ,nullable = True)
    partipante = database.Column(database.Integer, database.ForeignKey('projeto.id') ,nullable = True)
    

class Projeto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    descricao = database.Column(database.String, nullable = False)
    titulo = database.Column(database.String, nullable = False)
    link = database.Column(database.String, nullable = True, default = None)
    imagem = database.Column(database.String, nullable = False)
    projetos = database.relationship('Membros', backref='projeto', lazy= True)