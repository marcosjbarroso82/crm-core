import os

from django.db.models.signals import pre_delete, pre_save  # Import pre_save signal
from django.dispatch import receiver

from .models import CustomerPhoto


@receiver(pre_delete, sender=CustomerPhoto)
def delete_customer_photo(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(pre_save, sender=CustomerPhoto)
def delete_old_photo(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_photo = CustomerPhoto.objects.get(pk=instance.pk).photo
    except CustomerPhoto.DoesNotExist:
        return False

    new_photo = instance.photo
    if old_photo and old_photo != new_photo:
        if os.path.isfile(old_photo.path):
            os.remove(old_photo.path)
