from datetime import datetime
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(primary_key=True)

    create_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email

class message(models.Model):
    contact = models.ForeignKey(Contact, related_name="message_contact", on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    reply_success = models.BooleanField(default=0)

    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.contact.email} --- {self.reply_success}"