from apps.customer.models import Customer
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Set up initial user groups and permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        customer_manager_group, created = Group.objects.get_or_create(name='customer_manager')
        manager_group, created = Group.objects.get_or_create(name='manager')
        administrative_group, created = Group.objects.get_or_create(name='administrative')

        # Get all permissions for the Customer model
        content_type = ContentType.objects.get_for_model(Customer)
        permissions = Permission.objects.filter(content_type=content_type)

        # Assign permissions to groups
        customer_manager_group.permissions.set(permissions)
        manager_group.permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS('Successfully set up groups and permissions'))