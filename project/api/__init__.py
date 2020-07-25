from flask_restplus import Api

from project.api.ping import ping_namespace
from project.api.infoCarrera import infoCarrera_namespace
from project.api.top10 import top10_namespace
from project.api.infoCarreras import infoCarreras_namespace




api = Api(version="1.0", title="Onboarding", doc="/doc/")
api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(infoCarrera_namespace, path="/infoCarrera")
api.add_namespace(top10_namespace, path="/top10")
api.add_namespace(infoCarreras_namespace, path="/infoCarreras")
