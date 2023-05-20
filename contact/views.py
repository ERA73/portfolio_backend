from datetime import datetime
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import ContactSerializer
from .models import Contact, Message
from commons.functions import get_parameter, sent_email

# Models
from contact.models import Contact, Message

class ContactView(APIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def post(self, request, format=None):
        try:
            name = get_parameter("name", [request.query_params, request.data])
            email = get_parameter("email", [request.query_params, request.data])
            message = get_parameter("message", [request.query_params, request.data])
            
            current_contact = Contact.objects.filter(email = email).first()
            if current_contact:
                current_contact.updated_at = datetime.now()
                current_contact.save()
                new_message = Message.objects.create(contact = current_contact, content = message)
            else:
                current_contact = Contact.objects.create(name = name, email = email).first()
                new_message = Message.objects.create(contact = current_contact, content = message)

            sent_email("Message Received", [current_contact.email], "test message")
            
            return Response(status=201, data={"code":201, "message":"Correct"})
        except Exception as e:
            print(e)
            return Response(status=202, data={"code":202, "message":e.args[0]})