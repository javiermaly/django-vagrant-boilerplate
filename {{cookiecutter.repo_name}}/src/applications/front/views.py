# -*- coding: utf-8 -*-

"""
    Front app
    Author  :   {{cookiecutter.author_name}} <{{cookiecutter.email}}>
"""

from django.shortcuts import render


def index(request):
    """
        Index
    """
    return render(request, 'index.html', {})
