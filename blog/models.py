from django.db import models

# Create your models here.
class Hobbies(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField((""))
    image = models.CharField(
        max_length=500,
        blank=True,
        default="https://img.uline.com/is/image/uline/H-11295?$LargeRHD$",
    )

    def __str__(self):
        return f'<h3 style="font-weight:300">{self.name}: {self.description}</h3>\n'


class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField((""))
    image = models.CharField(
        max_length=500,
        blank=True,
        default="https://img.uline.com/is/image/uline/H-11295?$LargeRHD$",
    )

    def __str__(self):
        return f'<h3 style="font-weight:300">{self.name}: {self.description}</h3>\n'
