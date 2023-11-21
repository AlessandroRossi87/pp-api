from rest_framework import serializers
from .models import Plant
from reactions.models import Reaction


class PlantSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    reaction_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    hydrate_count = serializers.SerializerMethodField()
    moist_count = serializers.SerializerMethodField()
    drought_count = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_reaction_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            reaction = Reaction.objects.filter(
                owner=user, plant=obj
            ).first()
            return reaction.id if reaction else None
        return None

    def get_hydrate_count(self, obj):
        return obj.reactions.filter(reaction_type=1).count()

    def get_moist_count(self, obj):
        return obj.reactions.filter(reaction_type=2).count()

    def get_drought_count(self, obj):
        return obj.reactions.filter(reaction_type=3).count()

    class Meta:
        model = Plant
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'description', 'image', 'plant_children',
            'requested_children', 'taxonomy_choices', 'reaction_id',
            'hydrate_count', 'moist_count', 'drought_count',
            'comments_count',
        ]