# -*- coding: utf-8 -*-

"""
    Project settings for {{cookiecutter.project_name}}
    Author  :   {{cookiecutter.author_name}} <{{cookiecutter.email}}>
"""

from defaults import *
from getenv import env


INSTALLED_APPS += (
    'applications.front',
)

GRAPPELLI_ADMIN_TITLE = "Admin"

if not DEBUG:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
    AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')

BOWER_INSTALLED_APPS = (
    'jquery',
    'bootstrap'
)

PIPELINE_CSS = {
    'stylesheets': {
        'source_filenames': (
            'bootstrap/dist/css/bootstrap.min.css',
        ),
        'output_filename': 'stylesheets.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'scripts': {
        'source_filenames': (
            'jquery/dist/jquery.min.js',
            'bootstrap/dist/js/bootstrap.min.js',
        ),
        'output_filename': 'scripts.js',
    }
}
