from project import db
from passlib.hash import pbkdf2_sha256 as sha256

#soporte de base de datos 
class UserModel(db.Model): 
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    
    #Se guarda en la base de datos
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    #Se busca por usuario existente
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()
    
    #Devuelve todos los usuarios existentes
    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }
        return {'users': list(map(lambda x: to_json(x), UserModel.query.all()))}

    #Elimina todos los usuarios existentes
    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}
    
    #Genera una cadena hash que se almacena en la base de datos para proteger contraseña
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    #Verifica contraseña dada
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

#Control de tokens 
class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    
    #Se agrega token a la base de datos
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    #Verifica si el token es revocado
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)

