from rest_framework import serializers
from image.models import Image

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "uuid", "file")

    def create(self, validated_data):
        file = validated_data["file"]
        return Image.objects.create(
            original_name=file.name,
            file=file,
            content_type=file.content_type,
            size=file.size
        )
