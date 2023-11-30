from rest_framework import generics, permissions
from pp_api.permissions import IsOwnerOrReadOnly
from reactions.models import Reaction
from reactions.serializers import ReactionSerializer
from django.db.models import Count


class ReactionList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReactionSerializer
    queryset = Reaction.objects.values('reaction_type').annotate(reaction_count=Count('reaction_type'))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReactionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReactionSerializer
    queryset = Reaction.objects.all()