from django.db import models


'''
all model field url : https://docs.djangoproject.com/en/3.2/ref/models/fields/
django model field:
    - html widget
    - validation
    - db size
'''
# Create your models here.
class Job(models.Model): # Cryate table for database
    title = models.CharField(max_length=100) # Cryate Colume in table for database