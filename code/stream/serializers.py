from rest_framework import serializers
from .models import StreamRequest

class StreamRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamRequest
        fields = '__all__'

