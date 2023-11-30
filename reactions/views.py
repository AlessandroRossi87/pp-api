from rest_framework import generics, permissions
from pp_api.permissions import IsOwnerOrReadOnly
from reactions.models import Reaction
from reactions.serializers import ReactionSerializer
from django.db.models import Count


class ReactionList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReactionSerializer
    queryset = Reaction.objects.annotate(
        reactions_count_hydrate=Count('reaction_type', filter=reaction_type=1),
        reactions_count_moist=Count('reaction_type', filter=reaction_type=2),
        reactions_count_dry=Count('reaction_type', filter=reaction_type=3),
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReactionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReactionSerializer
    queryset = Reaction.objects.all()