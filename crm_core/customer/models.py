from django.core.exceptions import ValidationError
from django.db import models
import uuid
import os


def customer_photo_upload_to(instance, filename):
    # Use the instance's UUID as the filename
    return os.path.join('protected_media', 'customer', 'profile_photo', f"{instance.customer.uuid}.jpg")  # TODO: Change the extension to the uploaded file's extension


class Customer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='created_customers')
    updated_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='updated_customers')
    customer_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='active', choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return f"{self.name} {self.surname}"
    

def validate_photo(photo):
    file_size = photo.size
    limit_kb = 500
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)


class CustomerPhoto(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='photo')
    photo = models.ImageField(upload_to=customer_photo_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='created_customer_photos')
    updated_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='updated_customer_photos')
