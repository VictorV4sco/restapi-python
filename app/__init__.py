from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Instanciamos o db aqui (como um Bean do Spring)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    return app
