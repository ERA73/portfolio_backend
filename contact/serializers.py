from rest_framework import serializers
from .models import Contact, Message

class ContactSerializer(serializers.ModelSerializer):
    class Meta():
        model = Contact
        fields = '__all__'
        # fields = ('email', 'name', 'create_at', 'updated_at')