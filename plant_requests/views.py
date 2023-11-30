from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from plants.models import Plant
from .models import PlantRequest
from .serializers import PlantRequestSerializer
from pp_api.permissions import IsOwnerOrReadOnly


class NewPlantRequest(generics.ListCreateAPIView):
    serializer_class = PlantRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plant']

    def perform_create(self, serializer):
        plant_id = self.kwargs['plant_id']
        plant = Plant.objects.get(pk=plant_id)
        serializer.save(requester=self.request.user, plant=plant)

class ApprovePlantRequest(generics.UpdateAPIView):
    serializer_class = PlantRequestSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(is_approved=True)
        plant_request = PlantRequest.objects.get(pk=self.kwargs['pk'])
        plant_request.plant.plant_children -= 1
        plant_request.plant.save()