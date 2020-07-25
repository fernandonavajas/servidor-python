from flask_restplus import Namespace, Resource
from flask import request

top10_namespace = Namespace("top10")


class Top10(Resource):
    def post(self):
        entry_point = request.json
        error = False
        
        if error:
            return {"status": "error"}, 400, {'Server': '-'}
        nem = entry_point.get('nem','550') #cubre datos que no vienen ingresados
        return {"Nombre de Carrera": "nombre", "Codigo de Carrera": "codCarrera", "Nem": nem}, 200

top10_namespace.add_resource(Top10, "")
