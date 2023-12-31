from django.db.models import Count, Q
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from pp_api.permissions import IsOwnerOrReadOnly
from .models import Plant
from .serializers import PlantSerializer
from rest_framework.response import Response


class PlantList(generics.ListCreateAPIView):
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Plant.objects.annotate(
        comments_count=Count('comment', distinct=True),
        hydrate_count=Count('reactions', filter=Q(reactions__reaction_type=1)),
        moist_count=Count('reactions', filter=Q(reactions__reaction_type=2)),
        dry_count=Count('reactions', filter=Q(reactions__reaction_type=3)),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'reactions__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
        'taxonomy_choices',
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
        comments_count=Count('comment', distinct=True),
        hydrate_count=Count('reactions', filter=Q(reactions__reaction_type=1)),
        moist_count=Count('reactions', filter=Q(reactions__reaction_type=2)),
        dry_count=Count('reactions', filter=Q(reactions__reaction_type=3)),
    ).order_by('-created_at')


class TaxonomyChoices(generics.CreateAPIView):
    def get(self, request, *args, **kwargs):
        taxonomy_choices = [{'value': value, 'label': label} for value, label in Plant.taxonomy]
        return Response(taxonomy_choices)
