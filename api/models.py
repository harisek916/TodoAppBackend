from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todos(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="todos")
    title=models.CharField(max_length=200)
    options=(
        ('pending','pending'),
        ('inprogress','inprogress'),
        ('completed','completed')
    )
    status=models.CharField(max_length=200,choices=options,default='pending')
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)




