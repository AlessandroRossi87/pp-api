from rest_framework import serializers
from .models import Plant
from reactions.models import Reaction


class PlantSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Plant
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'description', 'image', 'plant_children', 
            'taxonomy_choices', 'comments_count',
        ]

class TaxonomyChoiceSerializer(serializers.Serializer):
    value = serializers.CharField(source='0')
    label = serializers.CharField(source='1') 