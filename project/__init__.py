from flask import Flask
from flask_cors import CORS
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
=======
from flask_swagger_ui import get_swaggerui_blueprint
from project.api import get_blueprint
>>>>>>> swagger-ui

cors = CORS()
db = SQLAlchemy()


def create_app(script_info=None):
    '''
    Inicia APP Flask para MS
    '''

    # instantiate the app
    app = Flask(__name__)

    ### swagger specific ###
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Seans-Python-Flask-REST-Boilerplate"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    ### end swagger specific ###


    app.register_blueprint(get_blueprint())

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
