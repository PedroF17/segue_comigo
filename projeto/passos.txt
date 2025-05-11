-- DOCUMENTOS --

(obter documentos)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\Scripts\activate
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install drf-writable-nested
pip install mysql-connector-python
pip install mysqlclient
django-admin startproject backend
python manage.py startapp projeto
python manage.py inspectdb > projeto/models.py
python manage.py makemigrations projeto
python manage.py migrate
python manage.py createsuperuser





-- DATABASE --

(Configurar PATH)
mysql -u root -p
CREATE DATABASE proj1;
(Instalar gestor de BDs)
(Importar DB do projeto)
