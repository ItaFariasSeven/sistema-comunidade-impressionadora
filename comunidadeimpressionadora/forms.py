from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, length
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Criar Senha', validators=[DataRequired(), Length(6,20)])
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    button_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail Já cadastrado. Cadastre-se com outro E-mail para continuar')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    remember_data = BooleanField('Lembrar dados de Acesso')
    button_submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    photo_perfil = FileField('Atualizar foto de perfil', validators=[FileAllowed(['jpg', 'png'])])
    course_excel = BooleanField('Excel Impressionador')
    course_vba = BooleanField('VBA Impressionador')
    course_powerbi = BooleanField('Power Bi Impressionador')
    course_python = BooleanField('Python Impressionador')
    course_ppt = BooleanField('Power Point Impressionador')
    course_sql = BooleanField('SQL Impressionador')
    button_submit_editperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail, cadastre outro e-mail')


class FormCriarPost(FlaskForm):
    title = StringField('Titulo do Post', validators=[DataRequired(), length(2, 100)])
    body = TextAreaField('Escreva seu Post Aqui', validators=[DataRequired()])
    button_submit = SubmitField('Criar Post')