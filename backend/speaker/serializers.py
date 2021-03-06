from rest_framework.serializers import ModelSerializer
from .models import Speaker


class SpeakerSerializer(ModelSerializer):
    class Meta:
        model = Speaker
        fields = ["id", "name", "position", "avatar"]
