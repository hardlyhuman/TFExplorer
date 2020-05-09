from rest_framework import serializers
from .models import API, APIVariant


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = ['name', 'usage', 'description', 'link']


class APIVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIVariant
        fields = ['api', 'usage', 'description']
