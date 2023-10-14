import os

from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random

from fakeapp.constanst import nickname, comment
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




@api_view(['GET'])
def life_chat(request):
    life = random.choice(nickname)
    comm = random.choice(comment)
    media_root = settings.MEDIA_ROOT
    media_path = os.path.join(media_root)
    images = [f for f in os.listdir(media_path) if f.endswith(".jpg")]
    if images:
        random_image = random.choice(images)
        image_url = os.path.join(random_image)
        full_image_url = request.build_absolute_uri(image_url)
        return Response({'username': life,
                         'comment': comm,
                         'image': full_image_url
                         }, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)