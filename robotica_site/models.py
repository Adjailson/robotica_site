##Banco de dados
from robotica_site import database
from flask_login import UserMixin
from datetime import datetime

class Noticias(database.Model):
    pass

class Usuario(database.Model, UserMixin):
    pass

class Projeto(database.Model):
    pass