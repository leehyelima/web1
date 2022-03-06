from django.db import models


class Menu (models.Model): 
    name = models.CharField(max_length=10)
    link = models.CharField(max_length=100)
    body = models.TextField(null=True)

    def __str__(self): 
        return f'{self.name}'