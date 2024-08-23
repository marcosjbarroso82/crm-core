from rest_framework import serializers

from crm_core.customer import models
from crm_core.user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class CustomerSerializer(serializers.ModelSerializer):

    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)

    class Meta:
        model = models.Customer
        fields = "__all__"
        read_only_fields = ('created_by', 'updated_by')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')

        try:
            full_photo_url = request.build_absolute_uri(f'/api/v1/customers/{instance.uuid}/photo/')
        except models.CustomerPhoto.DoesNotExist:
            full_photo_url = None

        representation['photo'] = full_photo_url

        return representation
