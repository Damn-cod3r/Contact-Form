from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.BigIntegerField() 
    message = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.full_name



