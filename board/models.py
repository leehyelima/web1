
from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Board(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False) 
    subject = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='posts', null=True)
    created_at= models.DateTimeField()
    

    def __str__(self):
        if self.user : return f'{self.user.get_username()}: {self.body}'
        else: return f'{self.body}'

