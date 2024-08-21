from rest_framework import serializers

from crm_core.user import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ["id", "username", "first_name", "last_name", "email", "is_staff", "is_active"]
