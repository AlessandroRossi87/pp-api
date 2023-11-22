from rest_framework import serializers
from .models import PlantRequest


class PlantRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantRequest
        fields = ['id', 'requester', 'plant', 'request_date', 'is_approved']