import django_filters

from fakeapp.models import FakeChat


class FakeChatFilter(django_filters.FilterSet):
    text = django_filters.CharFilter(field_name="text")

    class Meta:
        model = FakeChat
        fields = ['text']
