from django.contrib import admin

from fakeapp.models import FakeChat, FakePeople

# Register your models here.

admin.site.register(FakeChat)
admin.site.register(FakePeople)
