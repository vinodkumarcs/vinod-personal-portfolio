from django.contrib import admin

# Import Blog Class from models.py
from .models import Blog

admin.site.register(Blog)