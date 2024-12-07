from rest_framework import serializers 
from .models import RadioUser

class RadioUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadioUser
        fields = ['username', 'email', 'bio', 'birthday', 'profilePicture']


