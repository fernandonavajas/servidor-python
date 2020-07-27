import os

from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from project.api import get_blueprint

cors = CORS()



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
            'app_name': "Swagger API"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    ### end swagger specific ###


    app.register_blueprint(get_blueprint())

    # set config
    app.config.from_object("project.config.DevelopmentConfig")

    cors.init_app(app, resources={r"*": {"origins": "*"}})

    # register api
    from project.api import api
    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
