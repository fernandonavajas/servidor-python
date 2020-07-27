# Python 3.8.3

## 1. Crear virtual env
py -3 -m venv venv  # Windows

python3 -m venv venv  # Linux

## 2. Activar el virtual env
. venv/bin/activate  # Linux

venv\Scripts\activate  # Windows

# 3. Instalación
pip freeze > requirements.txt
 
pip install -r requirements.txt  

# 4. Levantar servidor
python manage.py run

# 5. App levantada!
Abre tu navegador: http://127.0.0.1:5000/ping