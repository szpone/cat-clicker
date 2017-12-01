from rest_framework import serializers
from .models import Click

class ClickSerializer(serializers.Serializer):

    class Meta:
        model = Click
        fields = '__all__'
