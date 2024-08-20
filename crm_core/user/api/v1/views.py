
from crm_core.user import models
from rest_framework.viewsets import ModelViewSet

from crm_core.user.api.v1.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ["username", "email", "first_name", "last_name"]