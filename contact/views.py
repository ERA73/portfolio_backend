import traceback
from datetime import datetime
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
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
                current_contact = Contact.objects.create(name = name, email = email)
                new_message = Message.objects.create(contact = current_contact, content = message)
            
            sent_email("Message Received", [current_contact.email], messaje=message, attach={"template":"contact.html", "data":{"name":name, "message":message}})
            new_message.reply_success = True
            new_message.save()
            return Response({"message":"Sent Successfully"})
        except Exception as e:
            traceback.print_exc()
            return Response({"message":"Something unexpected has occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)