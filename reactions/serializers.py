from rest_framework import serializers
from reactions.models import Reaction


class ReactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    reactions_count_hydrate = serializers.ReadOnlyField()
    reactions_count_moist = serializers.ReadOnlyField()
    reactions_count_dry = serializers.ReadOnlyField()

    reactions_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = Reaction
        fields = [
            'id', 'created_at', 'owner', 'plant', 'reaction_type',
            'reactions_count_hydrate', 'reactions_count_moist',
            'reactions_count_dry', 'reactions_id'
        ]
