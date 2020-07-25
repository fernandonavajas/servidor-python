from flask_restplus import Namespace, Resource
from flask import request

infoCarreras_namespace = Namespace("infoCarreras")


class InfoCarreras(Resource):
    def get(self):
        bar = request.args.to_dict()
        print (bar)        
        return {"Nombre de Carrera": "nombre", "Codigo de Carrera": "codCarrera", "Nem": "numero"}, 200

infoCarreras_namespace.add_resource(InfoCarreras, "")
