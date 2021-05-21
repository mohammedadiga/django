from django.db import models


'''
all django model field url : https://docs.djangoproject.com/en/3.2/ref/models/fields/
django model field:
    - html widget
    - validation
    - db size
'''
JOB_TYPE= (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

# Create your models here.
class Job(models.Model): # Create table for database
    title = models.CharField(max_length=100) # Create title Column in the table for database
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)# Create job_type Column in the table for database
    description = models.TextField(max_length=1000)# Create description Column in the table for database
    published_at = models.DateTimeField(auto_now=True)# Create published_at Column in the table for database
    Vacancy = models.IntegerField(default=1)# Create Vacancy Column in the table for database
    salary = models.IntegerField(default=0)# Create salary Column in the table for database
    experience = models.IntegerField(default=1) # Create experience Column in the table for database

    Category = models.ForeignKey('Category', on_delete=models.CASCADE) #Connect Category with table 



    # print title name in admin panel
    def __str__(self):
        return self.title

class Category(models.Model): # Create Category table for database
    name = models.CharField(max_length=25)# Create name Column in the Category table for database

        # print title name in admin panel
    def __str__(self):
        return self.name