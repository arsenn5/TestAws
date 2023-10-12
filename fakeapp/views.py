from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from fakeapp.filters import FakeChatFilter
from fakeapp.models import FakeChat
from fakeapp.serializers import FakeChatSerializer


# Create your views here.


@api_view(['GET'])
def fake_chat_view(request):
    queryset = FakeChat.objects.all()
    queryset = FakeChatFilter(request.GET, queryset=queryset).qs
    serializer = FakeChatSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)