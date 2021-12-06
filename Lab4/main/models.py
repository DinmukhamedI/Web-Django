from django.db import models

# Create your models here.

class Story(models.Model):
    username = models.CharField('User', max_length=10)
    mail = models.CharField('Email', max_length=50)
    date = models.DateTimeField('Date of buy')
    product = models.CharField('Product', max_length=20)

    def __str__(self):
        return self.username
