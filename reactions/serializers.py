from rest_framework import serializers
from reactions.models import Reaction


class ReactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reaction
        fields = ['id', 'created_at', 'owner', 'plant', 'reaction_type']