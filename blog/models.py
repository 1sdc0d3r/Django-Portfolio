from django.db import models

# Create your models here.
class Hobbies(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField((""))

    def __str__(self):
        return f'{self.name}: {self.description}'

class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField((""))

    def __str__(self):
        return f'{self.name}: {self.description}'
