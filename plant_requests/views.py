from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from plants.models import Plant
from .models import PlantRequest
from .serializers import PlantRequestSerializer
from pp_api.permissions import IsOwnerOrReadOnly


class NewPlantRequest(generics.ListCreateAPIView):
    queryset = PlantRequest.objects.all()
    serializer_class = PlantRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plant']

    def perform_create(self, serializer):
        plant_id = self.kwargs['plant_id']
        plant = Plant.objects.get(pk=plant_id)

        if plant.plant_children > 0:
            serializer.save(requester=self.request.user)
            plant.plant_children -= 1
            plant.save()
        else:
            return Response({"detail": "Unfortunately there are no plant children available."}, status=status.HTTP_400_BAD_REQUEST)

class ApprovePlantRequest(generics.UpdateAPIView):
    serializer_class = PlantRequestSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(is_approved=True)

        return Response({"detail": "Request approved."})

class DenyPlantRequest(generics.UpdateAPIView):
    serializer_class = PlantRequestSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(is_approved=False)

        return Response({"detail": "Request denied."})