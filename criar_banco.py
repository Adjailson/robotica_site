#Arquivo temporario para criar o banco de dados
from robotica_site import database, app
from robotica_site.models import *

with app.app_context():
    database.create_all()