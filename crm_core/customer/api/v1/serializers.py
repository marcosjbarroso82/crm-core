from rest_framework import serializers

from crm_core.customer import models
from crm_core.user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class CustomerSerializer(serializers.ModelSerializer):


    created_by = UserSerializer()
    updated_by = UserSerializer()

    class Meta:
        model = models.Customer
        fields = "__all__"


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')

        if instance.photo:
            full_photo_url = request.build_absolute_uri(f'/api/v1/customers/{instance.uuid}/photo/')
            representation['photo'] = full_photo_url
        else:
            representation['photo'] = None

        return representation

