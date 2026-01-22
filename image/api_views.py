from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
from .models import Image

class ImageUploadView(APIView):
    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.save()
            return Response(
                {"id": image.id, "uuid": image.uuid},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=400)

class ImageDetailView(APIView):
    def get(self, request, uuid):
        image = Image.objects.get(uuid=uuid)
        return Response({
            "id": image.id,
            "name": image.original_name,
            "url": image.file.url
        })

class ImageDeleteView(APIView):
    def delete(self, request, uuid):
        image = Image.objects.get(uuid=uuid)
        image.file.delete()
        image.delete()
        return Response(status=204)