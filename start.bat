@echo off

REM Activar el entorno virtual
call venv\Scripts\activate

REM Instalar las dependencias del proyecto
pip install -r requirements.txt

REM Ejecutar el servidor de desarrollo de Django
python manage.py runserver
