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
