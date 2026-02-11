from django.db import models

# Create your models here.
class Hobbies(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField((""))

    def __str__(self):
        return f'<h3 style="font-weight:300">{self.name}: {self.description}</h3>\n'

class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField((""))

    def __str__(self):
        return f'<h3 style="font-weight:300">{self.name}: {self.description}</h3>\n'
