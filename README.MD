

# Python 3.5

## 1. Crear virtual env
py -3 -m venv venv  # Windows

python3 -m venv venv  # Linux

## 2. Activar el virtual env
. venv/bin/activate  # Linux

venv\Scripts\activate  # Windows

# 3. Instalación
pip install -r requirements.txt  

# 4. Levantar servidor
python manage.py run

# 5. App levantada!
Abre tu navegador: http://127.0.0.1:5000/ping

# 6. Ver los servicios en Swagger
Abre tu navegador: http://127.0.0.1:5000/swagger

# 7. Registra un usuario y ocupa el access_token para consultar lo servicios con JWT
Abre tu navegador: http://127.0.0.1:5000/swagger/#/API%20AUTH/post_registration