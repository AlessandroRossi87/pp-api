from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Plant
from .serializers import PlantSerializer
from pp_api.permissions import IsOwnerOrReadOnly


class PlantList(APIView):
    serializer_class = PlantSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(
            plants, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PlantSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class PlantDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PlantSerializer

    def get_object(self, pk):
        try:
            plant = Plant.objects.get(pk=pk)
            self.check_object_permissions(self.request, plant)
            return plant
        except Plant.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        plant = self.get_object(pk)
        serializer = PlantSerializer(
            plant, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        plant = self.get_object(pk)
        serializer = PlantSerializer(
            plant, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        plant = self.get_object(pk)
        plant.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )