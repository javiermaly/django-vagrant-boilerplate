#! /bin/bash

echo "################################################"
echo "### Configure directories"
echo "################################################"

mkdir -p project/assets
mkdir -p project/locale
mkdir -p project/media

echo "################################################"
echo "### Configure database"
echo "################################################"

sudo -u postgres psql -c "CREATE USER $DJANGO_DATABASE_USER WITH PASSWORD '$DJANGO_DATABASE_PASSWORD';"
sudo -u postgres psql -c "CREATE DATABASE $DJANGO_DATABASE_NAME;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DJANGO_DATABASE_NAME to $DJANGO_DATABASE_USER;"
