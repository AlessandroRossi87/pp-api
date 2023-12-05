from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer, ContactFormSerializer
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        logging.debug(f"Contact created by user: {self.request.user}")

    def post(self, request, *args, **kwargs):
        logging.debug("Received POST request to /contact/")

        form_serializer = ContactFormSerializer(data=request.data)
        if form_serializer.is_valid():
            logging.debug("Contact form is valid")

            contact_serializer = ContactSerializer(data=form_serializer.validated_data)
            if contact_serializer.is_valid():
                logging.debug("Contact data is valid")

                contact_serializer.save(owner=request.user)
                logging.debug("Contact saved successfully")

                return Response(contact_serializer.data, status=status.HTTP_201_CREATED)
            else:
                logging.error(f"Contact data validation failed: {contact_serializer.errors}")
        else:
            logging.error(f"Contact form validation failed: {form_serializer.errors}")

        return Response(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)