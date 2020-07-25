

# Python 3.5

## Crear virtual env
py -3 -m venv venv  # Windows
python3 -m venv venv  # Linux

## Activar el virtual env
. venv/bin/activate  # Linux
venv\Scripts\activate  # Windows

# 3. Instalación
pip freeze > requirements.txt  
pip install -r requirements.txt  

# 4. Levantar servidor SOAP
python manage.py run