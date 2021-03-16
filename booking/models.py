from django.db import models
# Create your models here.


class MySiteUser(models.Model):
    name = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=64)
    image = models.ImageField(default="images/avatar.png",
                              null=True, blank=True, upload_to="images/")
    gender = models.CharField(max_length=64, null=True, blank=True)
    location = models.CharField(max_length=64, null=True, blank=True)
    postal_code = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return f"Name: {self.name} Email: {self.email}"
