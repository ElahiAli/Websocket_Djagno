from .models import Student
from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from django.forms.models import model_to_dict



@receiver(post_save, sender=Student)
def student_sender(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("Student", {'type':'change', 'text': json.dumps(model_to_dict(instance))})