from rest_framework import serializers
from reactions.models import Reaction


class ReactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    reactions_count_hydrate = serializers.ReadOnlyField()
    reactions_count_moist = serializers.ReadOnlyField()
    reactions_count_dry = serializers.ReadOnlyField()

    class Meta:
        model = Reaction
        fields = ['__all__']