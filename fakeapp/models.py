from django.db import models

from fakeapp.constanst import ANSWER, TEXT
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class FakeChat(models.Model):
    text = models.CharField(choices=TEXT, max_length=100)
    answer = models.CharField(choices=ANSWER, max_length=100)

    def __str__(self):
        return f'{self.text} - {self.id}'


class FakePeople(models.Model):
    avatar = models.ImageField(blank=True)
    phone_number = PhoneNumberField(max_length=100, unique=True, null=False)
    character = models.CharField(max_length=100)
    video = models.FileField()
    audio = models.FileField()
