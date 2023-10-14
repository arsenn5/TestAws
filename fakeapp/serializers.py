from rest_framework import serializers

from fakeapp.constanst import TEXT, ANSWER
from fakeapp.models import FakeChat, FakePeople


class FakeChatSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True)

    class Meta:
        model = FakeChat
        fields = 'id text answer'.split()


class FakeDogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakePeople
        fields = '__all__'

