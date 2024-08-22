import os

from django.http import FileResponse
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from crm_core.customer import models
from crm_core.customer.api.v1.serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_fields = ['customer_id', 'name', 'status']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    @action(detail=True, methods=['get', 'post', 'delete'], url_path='photo')
    def photo(self, request, pk=None):
        customer = self.get_object()
        try:
            customer_photo = customer.photo
        except models.CustomerPhoto.DoesNotExist:
            customer_photo = None

        if request.method == 'GET':
            if customer_photo and customer_photo.photo:
                customer.updated_by = self.request.user
                customer.save(update_fields=['updated_by'])
                return FileResponse(customer_photo.photo, content_type='image/jpeg')
            else:
                return Response(status=404)

        if request.method == 'POST':
            # Validate photo size
            file = request.FILES['photo']
            file_size = file.size
            limit_kb = 500
            if file_size > limit_kb * 1024:
                return Response({"error": "Max size of file is %s KB" % limit_kb}, status=400)

            if customer_photo:
                customer_photo.delete()

            customer.updated_by = self.request.user
            customer.save(update_fields=['updated_by'])
            # Save the new photo
            customer_photo = models.CustomerPhoto(customer=customer, photo=file)
            customer_photo.save()
            return Response(status=201)

        if request.method == 'DELETE':
            if customer_photo:
                customer_photo.delete()

                customer.updated_by = self.request.user
                customer.save(update_fields=['updated_by'])
                return Response(status=204)

            else:
                return Response(status=404)
