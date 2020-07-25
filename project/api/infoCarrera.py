from flask_restplus import Namespace, Resource
from flask import request

infoCarrera_namespace = Namespace("infoCarrera")


class InfoCarrera(Resource):
    def get(self):
        if not request.args.get('codCarrera'):
            return {"status": "error"}, 400
        codCarrera= request.args.get('codCarrera')
        return {"Nombre de Carrera": "nombre", "Codigo de Carrera": codCarrera, "Nem": "numero"}, 200

infoCarrera_namespace.add_resource(InfoCarrera, "")
