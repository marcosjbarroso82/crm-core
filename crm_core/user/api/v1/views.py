from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from crm_core.user import models
from crm_core.user.api.v1.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ["username", "email", "first_name", "last_name"]
    permission_classes = [IsAdminUser]

    @action(detail=True, methods=['post'], url_path='set-password')
    def set_password(self, request, pk=None):
        user = self.get_object()
        password = request.data.get('password')
        if not password:
            return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)

        user.password = make_password(password)
        user.save()
        return Response({'status': 'password set'}, status=status.HTTP_200_OK)
