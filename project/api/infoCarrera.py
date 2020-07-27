from flask_restplus import Namespace, Resource
from flask import request
from flask_jwt_extended import jwt_required

infoCarreras_namespace = Namespace("infoCarreras")
infoCarrera_namespace = Namespace("infoCarrera")
top10_namespace = Namespace("top10")


class InfoCarrera(Resource):
    @jwt_required
    def get(self):
        if not request.args.get('codCarrera'):
            return {"status": "error"}, 400
        codCarrera= request.args.get('codCarrera')
        return {"Nombre de Carrera": "nombre", "Codigo de Carrera": codCarrera, "Nem": "numero"}, 200


class Top10(Resource):
    @jwt_required
    def post(self):
        entry_point = request.json
        error = False
        
        if error:
            return {"status": "error"}, 400, {'Server': '-'}
        nem = entry_point.get('nem','550') #cubre datos que no vienen ingresados
        return {"Nombre de Carrera": "nombre", "Codigo de Carrera": "codCarrera", "Nem": nem}, 200


class InfoCarreras(Resource):
    @jwt_required
    def get(self):
        bar = request.args.to_dict()
        print (bar)        
        return {"Nombre de Carrera": "nombre", "Codigo de Carrera": "codCarrera", "Nem": "numero"}, 200


infoCarreras_namespace.add_resource(InfoCarreras, "")
infoCarrera_namespace.add_resource(InfoCarrera, "")
top10_namespace.add_resource(Top10, "")
