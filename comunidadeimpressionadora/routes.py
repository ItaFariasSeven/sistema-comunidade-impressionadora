from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora.models import Usuario, Post
from flask_login import login_user

lista_usuarios = ['lira', 'alessandro', 'josef']


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'button_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, form_login.password.data):
            login_user(usuario, remember=form_login.remember_data.data)
            flash(f'Login Feito com Sucesso no E-mail: {form_login.email.data}', 'alert-success')
            return redirect(url_for('home'))
        else:
            flash(f'Falha no Login E-mail ou Senha errados', 'alert-danger')
    if form_criarconta.validate_on_submit() and 'button_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.password.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, password=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta Criada para o E-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)