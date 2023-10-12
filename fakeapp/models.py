from django.db import models

from fakeapp.constanst import ANSWER, TEXT


# Create your models here.

class Text(models.Model):
    text = models.CharField(max_length=100)


class Answer(models.Model):
    answer = models.CharField(max_length=100)


class FakeChat(models.Model):
    text = models.CharField(choices=TEXT,max_length=100)
    answer = models.CharField(choices=ANSWER, max_length=100)
