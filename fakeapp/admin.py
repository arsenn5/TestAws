from django.contrib import admin

from fakeapp.models import FakeChat, Answer, Text

# Register your models here.

admin.site.register(FakeChat)
admin.site.register(Text)
admin.site.register(Answer)
