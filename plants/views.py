from django.db.models import Count
from rest_framework import generics, permissions, filters
from pp_api.permissions import IsOwnerOrReadOnly
from .models import Plant
from reactions.models import Reaction
from .serializers import PlantSerializer


class PlantList(generics.ListCreateAPIView):
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Plant.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'comments_count',
        'reactions__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Plant.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')