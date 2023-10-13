from rest_framework import serializers

from fakeapp.constanst import TEXT, ANSWER
from fakeapp.models import FakeChat, Image


class FakeChatSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True)

    # answer = AnswerSerializer()

    class Meta:
        model = FakeChat
        fields = 'id text answer'.split()


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')
