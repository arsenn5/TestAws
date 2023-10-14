import os
import random

from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from fakeapp.filters import FakeChatFilter
from fakeapp.models import FakeChat, FakePeople
from fakeapp.serializers import FakeChatSerializer, FakeDogSerializer


# Create your views here.


@api_view(['GET'])
@swagger_auto_schema(
    request_body=FakeChatSerializer,
    responses={200: "Success", 400: "Bad Request"},
)
def fake_chat_view(request):
    queryset = FakeChat.objects.all()
    queryset = FakeChatFilter(request.GET, queryset=queryset).qs
    serializer = FakeChatSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def fake_dog(request):
    queryset = FakePeople.objects.all()
    serializer = FakeDogSerializer(queryset, many=True, context={'request': request}).data
    return Response(data=serializer, status=status.HTTP_200_OK)

