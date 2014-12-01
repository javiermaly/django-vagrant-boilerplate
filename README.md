# Django Project Boilerplate

## ¿Qué contiene?

Contiene una maquina virtual con ubuntu 14.04 precofigurada para trabajar con Django y PostgreSQL.

El proyecto esta pensando para crear aplicaciones 12 factor http://12factor.net/

- Vagrant para generar el entorno de desarrollo https://www.vagrantup.com/
- Docker para generar un contenedor para producción https://www.docker.com/
- Django 1.7 como framework de desarrollo https://www.djangoproject.com/
- PostgreSQl como base de datos http://www.postgresql.org/
- PsycoPG2 como driver de postgres http://initd.org/psycopg/
- Pillow para manipulacion de imagenes https://pypi.python.org/pypi/Pillow/
- Django Debug Toolbar para un facil debug http://django-debug-toolbar.readthedocs.org/
- Django Pipeline para el manejo de assets y compresion de assets y html en producción http://django-pipeline.readthedocs.org/
- Django Storages para subir archivos a S3 u otro cloud storage https://django-storages.readthedocs.org/en/latest/
- Django Grappelli para customizar el panel de adimnistración http://grappelliproject.com/
- Django getenv para configurar via variables de entorno las settings del framework https://pypi.python.org/pypi/django-getenv
- Django bower para gestionar dependencias con bower https://django-bower.readthedocs.org/en/latest/
- Uwsgi para cargar la aplicación en un servidor http en docker https://uwsgi-docs.readthedocs.org/en/latest/
- Whitenoise para servir archivos estaticos https://github.com/evansd/whitenoise

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
