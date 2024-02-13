# toner_management_app/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Toner_Request

@receiver(post_save, sender=Toner_Request)
def update_toner_quantity(sender, instance, created, **kwargs):
    if instance.issued and instance.toner:
        instance.toner.quantity -= 1
        instance.toner.save()
