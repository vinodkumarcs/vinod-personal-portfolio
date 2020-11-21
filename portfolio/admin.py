from django.contrib import admin

# Import Project Class from models.py
from .models import Project

admin.site.register(Project)