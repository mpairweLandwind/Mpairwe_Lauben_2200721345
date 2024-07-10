from django.db import models

# Create your models here.
class Person(models.Model):
    user_number = models.PositiveIntegerField(default=23)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_profession = models.CharField(max_length=75)
    salaray = models.FloatField()

    def __str__(self) :
        return f'user:{self.first_name} {self.last_name}'

