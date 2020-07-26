from flask_restplus import Api

from project.api.ping import ping_namespace
from project.api.top10Carreras import top10_namespace
from project.api.infoCarreras import infoCarreras_namespace
from project.api.infoCarrera import infoCarrera_namespace
from project.api.authorization import userRegistration_namespace, userLogin_namespace, userLogoutAccess_namespace
from project.api.authorization import userLogoutRefresh_namespace, tokenRefresh_namespace, allUsers_namespace, secretResource_namespace

api = Api(version="1.0", title="API REST", doc="/doc/")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(top10_namespace, path="/top10")
api.add_namespace(infoCarreras_namespace, path="/infoCarreras")
api.add_namespace(infoCarrera_namespace, path="/infoCarrera")

# User Authorization
api.add_namespace(userRegistration_namespace, path="/registration")
api.add_namespace(userLogin_namespace, path="/login")
api.add_namespace(userLogoutAccess_namespace, path="/logout/access")
api.add_namespace(userLogoutRefresh_namespace, path="/logout/refresh")
api.add_namespace(tokenRefresh_namespace, path="/token/refresh")
api.add_namespace(allUsers_namespace, path="/users")
api.add_namespace(secretResource_namespace, path="/secret")