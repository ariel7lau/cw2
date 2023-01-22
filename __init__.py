from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['SECRET_KEY'] = '<2821fff32b1bded761d88900ae2714a8ca7884836b41b0589afd02eaaddfaa13>'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///comment.db'

    from portfolio.auth import auth
    app.register_blueprint(auth, url_prefix='/')
    
    return app