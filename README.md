# Django Project Boilerplate

## ¿Qué contiene?

Contiene una maquina virtual con ubuntu 14.04 precofigurada para trabajar con Django y PostgreSQL.


- Vagrant para generar el entorno de desarrollo https://www.vagrantup.com/
- Django 1.8rc1 como framework de desarrollo https://www.djangoproject.com/
- PostgreSQl como base de datos http://www.postgresql.org/
- PsycoPG2 como driver de Postgres http://initd.org/psycopg/
- Pillow para manipulacion de imagenes https://pypi.python.org/pypi/Pillow/
- Django Debug Toolbar para facilitar el debug de Django http://django-debug-toolbar.readthedocs.org/
- Django Compressor para comprimir archivos CSS y JS linkeados http://django-compressor.readthedocs.org/en/latest/
- Django HtmlMin para comprimir el HTML https://pypi.python.org/pypi/django-htmlmin
- Django Grappelli para customizar el panel de adimnistración http://grappelliproject.com/
- Django Getenv para configurar via variables de entorno las settings de Django https://pypi.python.org/pypi/django-getenv

## ¿Comó se usa?

Se necesita instalar cookiecutter (https://github.com/audreyr/cookiecutter)

    pip install cookiecutter

Y descargar con cookiecutter este template en el directorio donde quieras tener el proyecto


    cookiecutter https://github.com/nekrox/django-project-boilerplate

Se te haran unas preguntas para rellenar información acerca del template al contestarlas ya tendras una copia del template
lista para trabajar. Puedes leer el README.md incluido en el template del proyecto para saber como crear el entorno de desarrollo.

### Configurar Python y git con bash en Windows 7 ###

Instalar los siguientes paquetes para poder usar cookiecutter en windows

- Python 2.7 http://www.python.org/ftp/python/2.7.5/python-2.7.5.msi
- SetupTools para Python 2.7 http://www.lfd.uci.edu/~gohlke/pythonlibs/bnrm5n67/setuptools-1.1.6.win32-py2.7.exe
- Pip para Python 2.7 http://www.lfd.uci.edu/~gohlke/pythonlibs/bnrm5n67/pip-1.4.1.win32-py2.7.exe
- Pycrypto para Python 2.7 http://www.voidspace.org.uk/downloads/pycrypto26/pycrypto-2.6.win32-py2.7.exe
- Git con bash (decir que instale todo) http://msysgit.github.io/

Al terminar modificar en: Panel de Control > Sistema > Configuracion avanzada de Sistema
Despues en la pestaña de opciones avanzadas, dar click en variables de entorno.

Desplazarce hasta la variable "Path" hacer doble click y sin modificar la ruta solo le añadimos al final ;C:\Python27\Scripts
incluyendo el punto y coma, aceptamos todo.

NOTA: Todos los comandos que van a continuación se ejecutando dentro de la consola de git en si es una consola bash,
es necesario para poder usar ssh con vagrant y conectar a la maquina virtual.
