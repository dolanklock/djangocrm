from django.db import models

# CharField in Django is a small amount of text (someones name)
# TextField in Djnago is a lot of text (paragraph)

# see this link below for field types documentation django (scroll down to see methods "CharField")
# https://docs.djangoproject.com/en/1.11/ref/models/fields/

# always two step process when creating django database object. 1. create the model. and 2. migrate to the database (push into database)
# to push the migration you need to go to your terminal "git bash"
# make sure you are in correct directory so when you type "ls" you see manage.py, and then type these commands
# python manage.py makemigrations
# python manage.py migrate
# *make sure to add model to admin.py!!!

class ModelCRM(models.Model):  # all models need to inherit from models.Model
    first_name = models.CharField(max_length=100)  # CharField is a database datatype. Telling Django here what type of data will be stored in this field in the database
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    def __str__(self):  # need to return __str__ - this will be what is displayed on admin page and what will be displayed when you get data in views file and show on webpage!!!
        return f"{self.first_name}, {self.last_name}, {self.email}, {self.address}, {self.city}, {self.province}, {self.postal_code}"