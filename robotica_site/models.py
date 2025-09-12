##Banco de dados
from robotica_site import database, login_manager
from flask_login import UserMixin
from datetime import datetime
import pytz  

# Tabela de associação para relação muitos-para-muitos relacionar os membros aos projetos
membros_projeto = database.Table('membros_projeto',
    database.Column('membro_id', database.Integer, database.ForeignKey('membros.id', ondelete='CASCADE')),
    database.Column('projeto_id', database.Integer, database.ForeignKey('projeto.id', ondelete='CASCADE')),
    database.PrimaryKeyConstraint('membro_id', 'projeto_id')
)

@login_manager.user_loader
def load_usuario(id):
    return Usuario.query.get(int(id))

class Noticias(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    descricao = database.Column(database.Text, nullable=False) 
    titulo = database.Column(database.String(200), nullable=False)  
    link = database.Column(database.String(500), nullable=True, default=None)
    data_de_criacao = database.Column(database.DateTime, nullable=False, default=lambda: datetime.now(pytz.timezone('America')))
    imagem = database.Column(database.String(500), nullable=False)

    def __repr__(self):
        return f'<Noticia {self.titulo}>'

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    status = database.Column(database.Integer, default=1, nullable=False)  
    email = database.Column(database.String(120), nullable=False, unique=True)  
    senha = database.Column(database.String(200), nullable=False)  
    
    # Relação one-to-one com Membros e Usuario
    membro = database.relationship('Membros', backref='usuario', uselist=False, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Usuario {self.email}>'

class Membros(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False) 
    sobrenome = database.Column(database.String(100), nullable=False)  
    imagem = database.Column(database.String(500), nullable=True, default='default_avatar.png')
    descricao = database.Column(database.Text, nullable=True)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id', ondelete='CASCADE'), unique=True, nullable=True)
    
    # Relação muitos-para-muitos com Projeto e Membros
    projetos = database.relationship('Projeto', 
                                   secondary=membros_projeto,
                                   backref=database.backref('participantes', lazy='dynamic'),
                                   cascade='all, delete')

    def __repr__(self):
        return f'<Membro {self.nome} {self.sobrenome}>'

class Projeto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    descricao = database.Column(database.Text, nullable=False)
    titulo = database.Column(database.String(200), nullable=False)
    link = database.Column(database.String(500), nullable=True, default=None)
    imagem = database.Column(database.String(500), nullable=False, default='default_project.png')
    criador_id = database.Column(database.Integer, database.ForeignKey('usuario.id', ondelete='SET NULL'), nullable=True)

    def __repr__(self):
        return f'<Projeto {self.titulo}>'