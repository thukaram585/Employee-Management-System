from django.db import models
# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=30, null = False)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)


    def __str__(self):
        return self.first_name + "   " + self.last_name