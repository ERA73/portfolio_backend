from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contact, Message

# Create your views here.

class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()