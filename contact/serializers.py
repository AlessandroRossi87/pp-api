from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'owner', 'subject', 'content', 'link']

class ContactFormSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    content = serializers.CharField()
    link = serializers.CharField()