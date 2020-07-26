from flask_restplus import Namespace, Resource
from flask import request
from flask_jwt_extended import jwt_required

infoCarrera_namespace = Namespace("infoCarrera")


class InfoCarrera(Resource):
    @jwt_required
    def get(self):
        if not request.args.get('codCarrera'):
            return {"status": "error"}, 400
        codCarrera= request.args.get('codCarrera')
        return {"Nombre de Carrera": "nombre", "Codigo de Carrera": codCarrera, "Nem": "numero"}, 200


infoCarrera_namespace.add_resource(InfoCarrera, "")
