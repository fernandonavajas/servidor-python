from flask_restplus import Namespace, Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from project.model.models import UserModel

userRegistration_namespace = Namespace("userRegistration")
userLogin_namespace = Namespace("userLogin")
userLogoutAccess_namespace = Namespace("userLogoutAccess")
userLogoutRefresh_namespace = Namespace("userLogoutRefresh")
tokenRefresh_namespace = Namespace("tokenRefresh")
allUsers_namespace = Namespace("allUsers")
secretResource_namespace = Namespace("secretResource")

#análisis de datos entrantes 
parser = reqparse.RequestParser()
parser.add_argument('username', help = 'Este campo no puede ir vacio', required = True)
parser.add_argument('password', help = 'Este campo no puede ir vacio', required = True)


class UserRegistration(Resource): #Clase que registra a un usuario, en el body JSON username and password. (Content-type=application/json)
    def post(self):
        data = parser.parse_args()
        
        #Verifica si el usuario existe
        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}
        
        #Crea nuevo usuario
        new_user = UserModel(
            username = data['username'],
            password = UserModel.generate_hash(data['password'])
        )
        
        #Se guarda en la base de datos
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource): #Si el usuario existe, username y password en body, se puede logear (entrega access_token y refresh_token)
    def post(self):
        #Se analizan parametros de entrada
        data = parser.parse_args()
        #Se busca por nombre de usuario
        current_user = UserModel.find_by_username(data['username'])

        #Verifica si existe
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        #Se verifica contraseña
        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}

  
class UserLogoutAccess(Resource):  #Clase que invalida token de acceso
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):  #Clase que invalida refresh token
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500
      
      
class TokenRefresh(Resource): #Clase que solicita un nuevo token, con Headers Authorization Bearer <Token jwt>
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}
      
      
class AllUsers(Resource): #Obtiene todos los usuarios - elimina todos los usuarios
    @jwt_required
    def get(self):
        return UserModel.return_all()
    
    def delete(self):
        return UserModel.delete_all()
    
      
class SecretResource(Resource): #Se accede a ellos solo con un token
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }


userRegistration_namespace.add_resource(UserRegistration, "")
userLogin_namespace.add_resource(UserLogin, "")
userLogoutAccess_namespace.add_resource(UserLogoutAccess, "")
userLogoutRefresh_namespace.add_resource(UserLogoutRefresh, "")
tokenRefresh_namespace.add_resource(TokenRefresh, "")
allUsers_namespace.add_resource(AllUsers, "")
secretResource_namespace.add_resource(SecretResource, "")


