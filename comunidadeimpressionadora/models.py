#Banco de dados
from comunidadeimpressionadora import database, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    photo_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)
    courses = database.Column(database.String, nullable=False, default='Não Informado')

    def contar_posts(self):
        return len(self.posts)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    body = database.Column(database.Text, nullable=False)
    date_criation = database.Column(database.DateTime, nullable=False, default=datetime.now(timezone.utc))
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)