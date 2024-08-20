from rest_framework import serializers

from crm_core.customer import models
from crm_core.user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class CustomerPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomerPhoto
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    photo = CustomerPhotoSerializer()

    created_by = UserSerializer()
    updated_by = UserSerializer()

    class Meta:
        model = models.Customer
        fields = "__all__"
