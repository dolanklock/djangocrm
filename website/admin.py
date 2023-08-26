from django.contrib import admin
from . models import ModelCRM  # need to import stock class from models

# this will add a section in localhost:8000/admin page for new database
admin.site.register(ModelCRM)  # registers new Stock class model from Models file
