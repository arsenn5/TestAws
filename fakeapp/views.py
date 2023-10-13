import os
import random

from django.conf import settings
from django.contrib.staticfiles import finders
from django.http import FileResponse, JsonResponse
from django.urls import reverse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from fakeapp.filters import FakeChatFilter
from fakeapp.models import FakeChat, Image
from fakeapp.serializers import FakeChatSerializer, ImageSerializer


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


class RandomImage(APIView):
    def post(self, request):
        media_root = settings.MEDIA_ROOT
        media_path = os.path.join(media_root)
        images = os.listdir(media_path)
        if images:
            random_image = random.choice(images)
            image_url = os.path.join(random_image)
            full_image_url = request.build_absolute_uri(image_url)
            return Response({'image_url': full_image_url})
        else:
            return Response({'error': 'No images found in the media folder.'}, status=404)


class ImageView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
