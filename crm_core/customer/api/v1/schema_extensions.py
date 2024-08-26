# schema_extensions.py
from drf_spectacular.utils import extend_schema, OpenApiResponse
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample, OpenApiResponse
from django.http import FileResponse



customer_photo_get_schema = extend_schema(
        methods=['GET'],
        responses={
            200: OpenApiResponse(response=FileResponse, description='Customer photo retrieved successfully'),
            404: OpenApiResponse(description='Customer photo not found')
        }
    )
customer_photo_post_schema = extend_schema(
        methods=['POST'],
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'photo': {
                        'type': 'string',
                        'format': 'binary'
                    }
                },
                'required': ['photo']
            }
        },
        responses={
            'application/json': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string'
                    },
                    'error': {
                        'type': 'string'
                    }
                },
                'oneOf': [
                    {
                        'required': ['message']
                    },
                    {
                        'required': ['error']
                    }
                ]
            }
        },

        examples=[
            OpenApiExample(
                'Example Photo Upload',
                value={
                    'photo': 'example.jpg'
                },
                request_only=True,
                response_only=False
            )
        ]
    )
customer_photo_delete_schema = extend_schema(
        methods=['DELETE'],
        responses={
            204: OpenApiResponse(description='Customer photo deleted successfully'),
            404: OpenApiResponse(description='Customer photo not found')
        }
    )