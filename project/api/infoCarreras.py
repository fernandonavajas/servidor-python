from flask_restplus import Namespace, Resource
from flask import request
from flask_jwt_extended import jwt_required

infoCarreras_namespace = Namespace("infoCarreras")


class InfoCarreras(Resource):
    @jwt_required
    def get(self):
        bar = request.args.to_dict()
        lista = bar['codCarreras'].split(",")
        print (lista)        
        return {"Nombre de Carrera": "nombre", "Codigo de Carrera": "codCarrera", "Nem": "numero"}, 200

infoCarreras_namespace.add_resource(InfoCarreras, "")
