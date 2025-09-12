##Aqui é onde ficara o código dos formularios
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, FileField
from wtforms.validators import Length, DataRequired, EqualTo, Email, ValidationError
from robotica_site.models import Usuario

class FormLogin(FlaskForm):
    email = EmailField("Email", validators=[Length(max=50), Email(), DataRequired()])
    senha = PasswordField("Senha", validators=[Length(4,16), DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")
    

class FormCriarConta(FlaskForm):
    email = EmailField("Email", validators=[Length(max=50), Email(), DataRequired()])
    senha = PasswordField("Senha", validators=[Length(4,16), DataRequired()])
    confirmar_senha = PasswordField("Confirmar senha", validators=[Length(4,16), DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar conta")


    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email = email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado, faça login para continuar")
        
#Ainda em trabalho para adicionar usuarios cadastrados em membros
class FormMembroClube(FlaskForm):
    nome = StringField("Nome do membro", validators=[DataRequired()])
    sobrenome = StringField("Sobrenome do membro", validators=[DataRequired()])
    descricao = StringField("Descrição do membro", validators=[DataRequired()])
    imagem = FileField("Imagem", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Adicionar membro")

class FormNoticia(FlaskForm):
    titulo = StringField("Titulo da noticia", validators=[DataRequired()])
    descricao = StringField("Descrição da noticia", validators=[DataRequired()])
    link = StringField("Link da noticia (opcional)")
    imagem = FileField("Imagem", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Publicar noticia")

#Formulario de projetos ainda em trabalho. Precisa da opção de adicionar pessoas que participaram
class FormProjeto(FlaskForm):
    titulo = StringField("Titulo do projeto", validators=[DataRequired()])
    descricao = StringField("Descrição do projeto", validators=[DataRequired()])
    link = StringField("Link do projeto")
    imagem = FileField("Imagem", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Publicar projeto")