from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

cors = CORS()
db = SQLAlchemy()

def create_app(script_info=None):
    '''
    Inicia APP Flask para MS
    '''

    # instantiate the app
    app = Flask(__name__)

    # set config
    app.config.from_object("project.config.DevelopmentConfig")

    cors.init_app(app, resources={r"*": {"origins": "*"}})

    # setup db
    db.init_app(app)
    #Se crean la BD
    @app.before_first_request
    def create_tables():
        db.create_all()

    #JWT
    jwt = JWTManager(app)
    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        return False  

    
    # register api
    from project.api import api
    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "bd": bd}

    return app
