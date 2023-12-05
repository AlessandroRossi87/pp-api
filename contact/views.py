from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer, ContactFormSerializer

class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        

    def post(self, request, *args, **kwargs):
        form_serializer = ContactFormSerializer(data=request.data)
        if form_serializer.is_valid():
            contact_serializer = ContactSerializer(data=form_serializer.validated_data)
            if contact_serializer.is_valid():
                contact_serializer.save(owner=request.user)
                return Response(contact_serializer.data, status=status.HTTP_201_CREATED)
        return Response(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)