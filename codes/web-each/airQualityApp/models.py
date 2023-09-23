from django.db import models

# Create your models here.

class EmailList(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, error_messages={
        'unique': "This email has already been registered. Please use a different email."
    })
    gradClass = models.IntegerField()
