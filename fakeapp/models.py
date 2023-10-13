from django.db import models

from fakeapp.constanst import ANSWER, TEXT


# Create your models here.


class FakeChat(models.Model):
    text = models.CharField(choices=TEXT, max_length=100)
    answer = models.CharField(choices=ANSWER, max_length=100)

    def __str__(self):
        return f'{self.text} - {self.id}'

class Image(models.Model):
    image = models.ImageField(upload_to='media/')