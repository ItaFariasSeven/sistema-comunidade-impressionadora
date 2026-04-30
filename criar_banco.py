from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Post, Usuario

with app.app_context():
    database.create_all()