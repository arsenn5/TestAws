from django.contrib import admin

from fakeapp.models import FakeChat, Image

# Register your models here.

admin.site.register(FakeChat)
admin.site.register(Image)
