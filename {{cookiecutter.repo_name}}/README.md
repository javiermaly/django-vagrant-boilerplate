# {{cookiecutter.project_name}} #

{{cookiecutter.description}}

- AUTOR       :   {{cookiecutter.author_name}}
- EMAIL       :   {{cookiecutter.email}}
- URL         :   {{cookiecutter.domain_name}}
- EMPRESA     :   {{cookiecutter.company}}
- LICENCIA    :   {{cookiecutter.license}}
- VERSION     :   {{cookiecutter.version}}


## Como usar el entorno de desarrollo ##

### Instalar Vagrant ###

Vagrant y virtualbox se puede descargar de sus sitios para cualquier plataforma, si su sistema operativo (linux) tiene repositorios
que se pueden usar tambien.

- Virtual box: https://www.virtualbox.org
- Vagrant: http://www.vagrantup.com


### Configuración de archivos  ###

Este es el unico paso obligatorio para poder empezar a usar el entorno de desarrollo:

- Copiar __config/Envfile.example__ a __config/Envfile__ y editar las variables de entorno si es necesario.

Los siguientes pasos son opcionales:

- Para editar las configuraciones de django especificas del proyecto se puede editar __src/settings/project.py__.
- Si se necesitan instalar paquetes en el entorno de desarrollo se puede editar __config/packages.sh__.
- Si se necesita configurar algo en el entorno de desarrollo se puede editar __config/setup.sh__.
- Si se necesitan instalar paquetes en python se puede editar __src/requirements.txt__.
- Si se necesitan modificar el proceso que ejecuta la aplicación en docker se puede editar __src/Procfile__.
- Si se necesitan modificar los pasos de instalación de la aplicación en docker se puede editar __Dockerfile__.

### Manejando maquinas virtuales con vagrant ###

- Ejecutar __vagrant up__ para encender la maquina virtual la primera vez se instalan todos los paquetes necesarios.
- Ejecutar __vagrant ssh__ para entrar a la maquina virtual.
- Ejecutar __vagrant halt__ para apagar la maquina virtual.
- Ejecutar __vagrant reload__ para resetear la maquina virtual.
- Ejecutar __vagrant destroy__ para borrar la maquina virtual.

### Comandos para ejecutar dentro de la VM desde el host ###

- __bin/shell__ Muestra la shell de Django.
- __bin/runserver__ Ejecuta el servidor de desarrollo y se vuelve accesible por http://127.0.0.1:8000 en la maquina host.
- __bin/migrate__ Instala toda las migraciones en la base de datos.
- __bin/makemigrations__ Crea migraciones.
- __bin/makemessages \<paarametros\>__ Crea archivos de lenguaje.
- __bin/compilemessages__ Compila los archivos de lenguaje.
- __bin/startapp \<app-name\>__ Crea una nueva app.
- __bin/pip__ Instala todos los paquetes definidos en el requirements.txt.
- __bin/debugsqlshell__ Muestra la shell de debug-toolbar.
- __bin/bower \<commndo\>__ Maneja bower desde fuera de la VM usando django-bower.
- __bin/manage \<comando\>__ Ejecuta comandos con manage.py.
- __bin/exec \<comando\>__ Ejecuta comandos en bash.
- __bin/psql__ Ejecuta la shell de postgres.
- __bin/pgweb__ Ejecuta pgweb un frontend web para postgres accesible desde http://localhost:5000.

### Workflow de ejemplo ###

#### Creando el entorno de desarrollo para el proyecto ####

- Ejecutar __vagrant up__ para crear la maquina virtual y provisionarla con todo lo necesario.
- Ejecutar __bin/migrate__ para crear las tablas principales.
- Ejecutar __bin/createsuperuser__ para crear el usuario de administración.
- Ejecutar __bin/bower__ para instalar las dependencias del frontend.
- Ejecutar __bin/runserver__ para correr el servidor de desarrollo.

NOTA: Para para poder acceder a la aplicación se hace por http://127.0.0.1:8000.

#### Retomando el desarrollo ya existente en un equipo ####

- Ejecutar __vagrant up__ para encender la maquina virtual.
- Ejecutar __bin/migrate__ para actualizar la base de datos en caso de usar migraciones.
- Ejecutar __bin/bower__ para instalar las dependencias del frontend.
- Ejecutar __bin/runserver__ para correr el servidor de desarrollo.

## Deployment con Docker ##

Para crear la imagen contenedora para producción solo es necesario crearla con docker

```
  docker build -t company/app-name .
```

Y correr la imagen para generar un contenedor

```
  docker run -d -p 8000:8000 -e 'DJANGO_DEBUG=False' -e 'DJANGO_DATABASE_HOST=host.com' -e 'DJANGO_DATABASE_PORT=5432' -e 'DJANGO_DATABASE_NAME=test' -e 'DJANGO_DATABASE_USER=test' -e 'DJANGO_DATABASE_PASSWORD=test' -e 'DJANGO_EMAIL_HOST_USER=user@host.com' -e 'DJANGO_EMAIL_HOST_PASSWORD=mypassword' -e 'DJANGO_EMAIL_HOST=smtp.host.com' -e 'DJANGO_EMAIL_USE_TLS=True' -e 'DJANGO_EMAIL_PORT=587' company/app-name
```
