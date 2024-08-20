from rest_framework import serializers

from crm_core.user import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = "__all__"
