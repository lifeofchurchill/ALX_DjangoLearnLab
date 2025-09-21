from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.apps import AppConfig




class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'
