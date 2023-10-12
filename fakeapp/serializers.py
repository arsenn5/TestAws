from rest_framework import serializers

from fakeapp.constanst import TEXT, ANSWER
from fakeapp.models import FakeChat, Text, Answer


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['text']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer']


class FakeChatSerializer(serializers.ModelSerializer):
    # text = TextSerializer()
    # answer = AnswerSerializer()

    class Meta:
        model = FakeChat
        fields = 'id text answer'.split()
