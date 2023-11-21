from rest_framework import generics, permissions
from pp_api.permissions import IsOwnerOrReadOnly
from .models import Plant
from .serializers import PlantSerializer


class PlantList(generics.ListCreateAPIView):
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Plant.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Plant.objects.all()