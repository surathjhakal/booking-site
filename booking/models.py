from django.db import models
# Create your models here.


class MySiteUser(models.Model):
    name = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=64)
    password_again = models.CharField(max_length=64)

    def __str__(self):
        return f"Name: {self.name} Email: {self.email}"
